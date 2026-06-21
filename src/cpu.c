#include <stdio.h>   // For printf and file operations (fopen, fscanf)
#include <stdlib.h>  // For the exit() function
#include <unistd.h>  // For the sleep()/usleep() functions

// This function reads the system time "ticks" from /proc/stat
void get_cpu_stats(long long *idle, long long *total) {
    // Open the virtual file /proc/stat. It lives in RAM, not on the disk
    FILE *fp = fopen("/proc/stat", "r");
    if (!fp) {
        perror("Error opening /proc/stat");
        exit(1);
    }

    char cpu_label[10];
    long long user, nice, system, idle_val, iowait, irq, softirq, steal;

    /**
     * fscanf reads the first line of /proc/stat which looks like:
     * cpu  2255 34 2290 2262556 ...
     * Each number represents the time the CPU has spent in a specific state.
     */
    fscanf(fp, "%s %lld %lld %lld %lld %lld %lld %lld %lld", // lld (Long Long decimal)
           cpu_label, // Reads the word "cpu"
           &user,     // User processes
           &nice,     // Low priority (nice) processes
           &system,   // Kernel (system) processes
           &idle_val, // Idle time (the most important one)
           &iowait,   // Waiting for I/O (disk/network)
           &irq,      // Hardware interrupts
           &softirq,  // Software interrupts
           &steal);   // Time "stolen" by the hypervisor (in virtual machines)

    // The "idle" time is the sum of staying free (idle) and waiting for I/O.
    *idle = idle_val + iowait; // the * indicates dereferencing/pointer target

    // The total time is the sum of absolutely all columns
    *total = user + nice + system + idle_val + iowait + irq + softirq + steal;

    fclose(fp); // Close the "file" to free the descriptor
}

int main() {
    long long idle1, total1, idle2, total2;

    // Capture the initial state
    get_cpu_stats(&idle1, &total1);

    // Wait for a short duration (100ms)
    usleep(100000); 

    // Capture the final state
    get_cpu_stats(&idle2, &total2);

    // Calculate differences
    long long total_diff = total2 - total1;
    long long idle_diff = idle2 - idle1;

    if (total_diff == 0) { // Safety guard. Do not divide by zero.
        printf("0.00%%");
        return 0;
    }

    double usage = 100.0 * (total_diff - idle_diff) / total_diff;

    // Print ONLY the percentage so Python can parse it easily
    printf("%.2f%%", usage);
    
    return 0; // Terminate and return control to Python
}
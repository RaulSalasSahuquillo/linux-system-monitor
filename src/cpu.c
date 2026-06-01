#include <stdio.h>   // Para printf y operaciones de archivos (fopen, fscanf)
#include <stdlib.h>  // Para la función exit()
#include <unistd.h>  // Para la función sleep()

// Esta función lee los "tics" de tiempo del sistema desde /proc/stat
void get_cpu_stats(long long *idle, long long *total) {
    // Abre el archivo virtual /proc/stat. No está en el disco, vive en la RAM
    FILE *fp = fopen("/proc/stat", "r");
    if (!fp) {
        perror("Error al abrir /proc/stat");
        exit(1);
    }

    char cpu_label[10];
    long long user, nice, system, idle_val, iowait, irq, softirq, steal;

    /**
     * fscanf lee la primera línea de /proc/stat que se ve así:
     * cpu  2255 34 2290 2262556 ...
     * * Cada número representa el tiempo que la CPU ha pasado en un estado específico
     */
    fscanf(fp, "%s %lld %lld %lld %lld %lld %lld %lld %lld", // lld (Long Long decimal)
           cpu_label, // Lee la palabra "cpu"
           &user,     // Procesos de usuario
           &nice,     // Procesos de baja prioridad
           &system,   // Procesos del kernel (sistema)
           &idle_val, // Tiempo de inactividad (el más importante)
           &iowait,   // Esperando a discos/red
           &irq,      // Interrupciones de hardware
           &softirq,  // Interrupciones de software
           &steal);   // Tiempo "robado" por el hipervisor (en máquinas virtuales)

    // El tiempo "ocioso" es la suma de estar libre (idle) y esperar I/O.
    *idle = idle_val + iowait; // el * indica que es dirección de memoria

    // El tiempo total es la suma de absolutamente todas las columnas
    *total = user + nice + system + idle_val + iowait + irq + softirq + steal;

    fclose(fp); // Cerramos el "archivo" para liberar el descriptor
}

int main() {
    long long idle1, total1, idle2, total2;

    // Captura el estado inicial
    get_cpu_stats(&idle1, &total1);

    // Espera un tiempo corto (100ms)
    usleep(100000); 

    // Captura el estado final
    get_cpu_stats(&idle2, &total2);

    // Calcula la diferencia
    long long total_diff = total2 - total1;
    long long idle_diff = idle2 - idle1;

    if (total_diff == 0) { // Mejor no tocar. Funciona, eso es lo importante
        printf("0.00%%");
        return 0;
    }

    double usage = 100.0 * (total_diff - idle_diff) / total_diff;

    // Imprime SOLO el número para que Python lo lea fácil
    printf("%.2f%%", usage);
    
    return 0; // El programa termina y le devuelve el control a Python
}
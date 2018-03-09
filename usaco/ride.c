/*
ID: aditya15
LANG: C
PROG: ride
*/
#include <stdio.h>
main () {
    
    FILE *fin  = fopen ("ride.in", "r");
    FILE *fout = fopen ("ride.out", "w");
    
    char * a, b;

    fscanf (fin, "%s %s", &a, &b);	/* the two input integers */
    fprintf (fout, "%d\n", a+b);
    exit (0);
}

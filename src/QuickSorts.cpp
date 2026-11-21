#include "QuickSorts.h"

#include <cstdlib>

void SinglePivotQuickSort(int* arr, int n)
{
    if (n<2) return;

int p = rand() % n;
int P = arr[p];

arr[p] = arr[n - 1];
arr[n - 1] = P;

int i, j;
i = j = 0;
while(j < n)
{
    if (arr[j] <= P)
    {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
        i++;
    }
    
    j++;
}

int pivotPos = i -1;

SinglePivotQuickSort(arr, pivotPos);
SinglePivotQuickSort(arr + pivotPos + 1, n - pivotPos - 1);
}
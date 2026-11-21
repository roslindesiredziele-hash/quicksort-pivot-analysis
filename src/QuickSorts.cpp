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

void DualPivotQuickSort(int* arr, int n)
{
    if (n < 2)
    {
        return;
    }

    if (arr[0] > arr[n - 1])
    {
        int t = arr[0];
        arr[0] = arr[n - 1];
        arr[n - 1] = t;
    }

    int pivot1 = arr[0];
    int pivot2 = arr[n - 1];

    int lt = 1;
    int gt = n - 2;
    int i = 1;

    while (i <= gt)
    {
        if (arr[i] < pivot1)
        {
            int t = arr[i];
            arr[i] = arr[lt];
            arr[lt] = t;

            lt++;
        }
        else if (arr[i] > pivot2)
        {
            while (i < gt &&
                   arr[gt] > pivot2)
            {
                gt--;
            }

            int t = arr[i];
            arr[i] = arr[gt];
            arr[gt] = t;

            gt--;

            if (arr[i] < pivot1)
            {
                t = arr[i];
                arr[i] = arr[lt];
                arr[lt] = t;

                lt++;
            }
        }

        i++;
    }

    lt--;
    gt++;

    int t = arr[0];
    arr[0] = arr[lt];
    arr[lt] = t;

    t = arr[n - 1];
    arr[n - 1] = arr[gt];
    arr[gt] = t;

    DualPivotQuickSort(arr, lt);

    DualPivotQuickSort(arr + lt + 1, gt - lt - 1);

    DualPivotQuickSort(arr + gt + 1, n - gt - 1);
}
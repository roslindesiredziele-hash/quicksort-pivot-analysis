#include "QuickSorts.h"

#include <Windows.h>

#include <iostream>
#include <fstream>
#include <ctime>

using namespace std;

int* GenerateRandomArray(int n);
double MeasureSinglePivot(int n, int repetitions);
double MeasureDualPivot(int n, int repetitions);

int main()
{
    srand(time(nullptr));

    int data[] =
{
    5, 1, 8, 3, 2, 9, 4
};

int data1[] = {
    7, 1, 5, 3, 2, 9, 4
};

SinglePivotQuickSort(data, 7);

for (int i = 0; i < 7; i++)
{
    cout << data[i] << " ";
}

cout << endl;

DualPivotQuickSort(data1, 7);

for (int i = 0; i < 7; i++)
{
    std::cout << data1[i] << " ";
}

cout << endl;

    return 0;
}

int* GenerateRandomArray(int n)
{
    int* arr = new int[n];

    for (int i = 0; i < n; i++)
    {
        arr[i] = rand();
    }

    return arr;
}

double MeasureSinglePivot(int n, int repetitions)
{
    LARGE_INTEGER start, end, frequency;

    QueryPerformanceFrequency(&frequency);

    double totalTime = 0.0;

    for (int r = 0; r < repetitions; r++)
    {
        int* original = GenerateRandomArray(n);

        int* arr = new int[n];

        for (int i = 0; i < n; i++)
        {
            arr[i] = original[i];
        }

        QueryPerformanceCounter(&start);

        SinglePivotQuickSort(arr, n);

        QueryPerformanceCounter(&end);

        totalTime += (end.QuadPart - start.QuadPart) * 1000.0 / frequency.QuadPart;

        delete[] arr;
        delete[] original;
    }

    return totalTime / repetitions;
}

double MeasureDualPivot(int n, int repetitions)
{
    LARGE_INTEGER start, end, frequency;

    QueryPerformanceFrequency(&frequency);

    double totalTime = 0.0;

    for (int r = 0; r < repetitions; r++)
    {
        int* original = GenerateRandomArray(n);

        int* arr = new int[n];

        for (int i = 0; i < n; i++)
        {
            arr[i] = original[i];
        }

        QueryPerformanceCounter(&start);

        DualPivotQuickSort(arr, n);

        QueryPerformanceCounter(&end);

        totalTime += (end.QuadPart - start.QuadPart) * 1000.0 / frequency.QuadPart;

        delete[] arr;
        delete[] original;
    }

    return totalTime / repetitions;
}
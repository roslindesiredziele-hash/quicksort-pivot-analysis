#include "QuickSorts.h"

#include <Windows.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>

using namespace std;

int* GenerateRandomArray(int n);
void MeasureSorts( int n, int repetitions, double& singleTime, double& dualTime);

int main()
{
    srand(time(nullptr));

    ofstream outfile("./data/data.csv");

    if (!outfile)
    {
        cerr
            << "Unable to open benchmark.csv\n";

        return 1;
    }

    outfile << "Size," << "SinglePivotMs," << "DualPivotMs\n";

    vector<int> sizes =
{
    5,
    10,
    15,
    20,
    25,
    30,
    35,
    40,
    45,
    50,
    100,
    150,
    200,
    300,
    400,
    500,
    1000,
    2000,
    3000,
    4000,
    5000,
    10000,
    20000,
    50000,
    100000
};

    for (int size : sizes)
    {
        int repetitions;

        if (size <= 1000)
        {
            repetitions = 1000;
        }
        else if (size <= 10000)
        {
            repetitions = 200;
        }
        else
        {
            repetitions = 50;
        }

        double singleTime = MeasureSinglePivot( size, repetitions);

        double dualTime = MeasureDualPivot(size, repetitions);

        cout << "Size: " << size << " | Single Pivot: " << singleTime << " ms" << " | Dual Pivot: " << dualTime << " ms" << endl;

        outfile << size << "," << singleTime << "," << dualTime << "\n";
    }

    outfile.close();

    cout << "\nBenchmark completed.\n";

    cout << "Results saved to " << "./data/data.csv\n";

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
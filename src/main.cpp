#include "QuickSorts.h"

#include <iostream>
#include <ctime>

using namespace std;



int main()
{
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
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

QuickSort(data, 7);

for (int i = 0; i < 7; i++)
{
    cout << data[i] << " ";
}

    return 0;
}
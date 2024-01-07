#include <iostream>
#include <vector>

using namespace std;

vector<int> selection_sort(vector<int>array) {
    int min_num; int min_index; int temp;
    for (int i=0; i<array.size()-1; i++) {
        min_num = array[i]; min_index = i;
        for (int j=i+1; j<array.size(); j++) {
            if (min_num > array[j]) {
                min_num = array[j]; min_index = j;
            }
        }
        if (min_index != i) {
            temp = array[i];
            array[i] = array[min_index];
            array[min_index] = temp;
        }
    }
    return array;
}

int main() {
    vector<int>arr; cout << "Length of array: ";
    int x; int l; cin >> l;
    for (int k=0; k<l; k++) {
        cin >> x;
        arr.push_back(x);
    }
    cout << "Given array: ";
    for (int i : arr)
        cout << i << " ";
    cout << endl;
    vector<int>arr2;
    arr2 = selection_sort(arr);
    cout << "Sorted array: ";
    for (int j : arr2)
        cout << j << " ";
    cout << endl;
    return 0;
}
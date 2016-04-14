#include<stdio.h>
#include<stdlib.h>
int longes_s(int arr[],int n){
    int *temp = (int*) malloc ( sizeof( int ) * n );
    int result = 0;
    // initialize temp 0 so it can be use to compute in the loop
    temp[0] = 1;
    for (int i = 1; i < n; i++){
        temp[i]=1;
        for (int j = 0; j < i;j++){
            if(arr[j]<arr[i]){
                if(temp[j]>=temp[i]){
                    temp[i]=temp[j]+1;
                    if (result<temp[i]){
                        // get the longest result here to avoid to use another for loop later
                        result = temp[i];
                    }
                }
            }
        }
    }
    free(temp);
    return result;
}
int main()
{
    int arr[] = { 10, 22, 9, 33, 21, 50, 41, 60 };
    int n = sizeof(arr)/sizeof(arr[0]);


    printf("Length of LIS is %d\n",  longes_s( arr, n ));
    return 0;
}

#include<bits/stdc++.h>
using namespace std;
class solution{
     public:
     vector<long long>seg;
     vector<long long>ar;
     solution(long long n){
          seg.resize(4*n,0);
          ar.resize(n,0);
     }
     void build(long long node,long long low,long long high,long long arr[]){
          if(low==high){
               seg[node]=1;
               ar[low]=arr[low];
               return;
          }
          long long mid=(low+high)>>1;
          build(2*node+1,low,mid,arr);
          build(2*node+2,mid+1,high,arr);
          seg[node]=seg[2*node+1]+seg[2*node+2];
          return;
     }
     long long update(long long node,long long low,long long high,long long position){
          if(low==high){
               seg[node]=0;
               return ar[low];
          }
          long long res;
          long long mid=(low+high)>>1;
          if(position<=seg[2*node+1]){
               res=update(2*node+1,low,mid,position);
          }
          else{
               res=update(2*node+2,mid+1,high,position-seg[2*node+1]);
          }
          seg[node]=seg[2*node+1]+seg[2*node+2];
          return res;
     }
};
int main(){
     long long n;
     cin>>n;
     long long arr[n];
     long long res[n];
     for(int i=0; i<n; i++){
          cin>>arr[i];
     }
     solution st(n);
     st.build(0,0,n-1,arr);
     for(int j=0; j<n; j++){
          long long removal;
          cin>>removal;
          res[j]=st.update(0,0,n-1,removal);
     }
     for(int k=0; k<n; k++){
          cout<<res[k]<<" ";
     }
     return 0;
}
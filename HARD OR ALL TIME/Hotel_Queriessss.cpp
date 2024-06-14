#include<bits/stdc++.h>
using namespace std;
class Solution{
     public:
     vector<long long>seg;
     Solution(long long n){
          seg.resize(4*n,0);
     }
     void build(long long node,long long low,long long high,long long arr[]){
          if(low==high){
               seg[node]=arr[low];
               return;
          }
          long long mid=(low+high)>>1;
          build(2*node+1,low,mid,arr);
          build(2*node+2,mid+1,high,arr);
          seg[node]=max(seg[2*node+1],seg[2*node+2]);
          return;
     }
     long long solve(long long node,long long low,long long high,long long room){
          if(low==high){
               seg[node]-=room;
               return low+1;
          }
          long long mid=(low+high)>>1;
          long long index=-1;
          if(seg[2*node+1]>=room){
               index=solve(2*node+1,low,mid,room);
          }
          else{
               index=solve(2*node+2,mid+1,high,room);
          }
          seg[node]=max(seg[2*node+1],seg[2*node+2]);
          return index;

     }
     long long upsolve(long long val){
          return (seg[0]>=val);
     }
};
int main(){
     long long n,m;
     cin>>n>>m;
     long long arr[n];
     vector<long long>res(m,0);
     for(long long i=0; i<n; i++){
          cin>>arr[i];
     }
     Solution st(n);
     st.build(0,0,n-1,arr);
     for(long long j=0; j<m; j++){
          long long group;
          cin>>group;
          if (st.upsolve(group)){
               res[j]=st.solve(0,0,n-1,group);
          }
     }
     for(long long k=0; k<m; k++){
          cout<<res[k]<<" ";
     }
     return 0;
}
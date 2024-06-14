#include<bits/stdc++.h>
using namespace std;
class solution{
public:
     vector<long long >seg;
     vector<long long>lazy;
     solution(long long n){
          seg.resize(4*n,0);
          lazy.resize(4*n,0);
     }
     void segment(long long node,long long  low,long long high,long long arr[]){
          if(low==high){
               seg[node]=arr[low];
               return;
          }
          long long mid=(low+high)>>1;
          segment(2*node+1,low,mid,arr);
          segment(2*node+2,mid+1,high,arr);
          seg[node]=seg[2*node+1]+seg[2*node+2];
          return;
     }
     void up(long long node,long long low,long long high){
          seg[node]+=(lazy[node]*(high-low+1));
          if (low!=high){
               lazy[2*node+1]+=lazy[node];
               lazy[2*node+2]+=lazy[node];
          }
          lazy[node]=0;
          return;
     }
     void update(long long node,long long low,long long high,long long l,long long r,long long val){
          if(low>r || high<l){
               return;
          }
          if(low>=l && high<=r){
               lazy[node] +=val;
               return;
          }
          long long mid=(low+high)>>1;
          update(2*node+1,low,mid,l,r,val);
          update(2*node+2,mid+1,high,l,r,val);
          seg[node]=seg[2*node+1]+seg[2*node+2];
          return;
     }
     long long getval(long long node,long long low,long long high,long long position){
          if (lazy[node]!=0){
               up(node,low,high);
          }
          if(low==high){
               return seg[node];
          }
          long long mid=(low+high)>>1;
          if (position<=mid){
               return getval(2*node+1,low,mid,position);
          }
          return getval(2*node+2,mid+1,high,position);
     }
};
int main(){
     long long n,q;
     cin>>n>>q;
     long long arr[n];
     for(long long i=0; i<n; i++){
          cin>>arr[i];
     }
     solution st(n);
     st.segment(0,0,n-1,arr);
     while (q--){
          int  type;
          cin>>type;
          if (type==1){
               long long a,b,val;
               cin>>a>>b>>val;
               st.update(0,0,n-1,a-1,b-1,val);
          }
          else{
               long long index;
               cin>>index;
               cout<<st.getval(0,0,n-1,index-1)<<endl;
          }
     }
     return 0;
}
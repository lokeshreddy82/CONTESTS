#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    long long dp[105][105][105];
    long long maxValue(int i, int firstj, int secondj, vector<vector<pair<long long,long long>>>&arr){
        if(i==arr.size())return -1e11;
        if(dp[i][firstj+1][secondj+1]!=-1){
            return dp[i][firstj+1][secondj+1];
        }
        long long ans=LONG_LONG_MIN;
        if(firstj==-1){
            ans=max(ans,maxValue(i+1,firstj,secondj,arr));
            ans=max(ans,arr[i][0].first+maxValue(i+1,arr[i][0].second,secondj,arr));
            ans=max(ans,arr[i][1].first+maxValue(i+1,arr[i][1].second,secondj,arr));
            ans=max(ans,arr[i][2].first+maxValue(i+1,arr[i][2].second,secondj,arr));
        }
        else if(secondj==-1){
            ans=max(ans,maxValue(i+1,firstj,secondj,arr));
            if(arr[i][0].second!=firstj)
            ans=max(ans,arr[i][0].first+maxValue(i+1,firstj,arr[i][0].second,arr));
            if(arr[i][1].second!=firstj)
            ans=max(ans,arr[i][1].first+maxValue(i+1,firstj,arr[i][1].second,arr));
            if(arr[i][2].second!=firstj)
            ans=max(ans,arr[i][2].first+maxValue(i+1,firstj,arr[i][2].second,arr));
        }
        else{
            ans=max(ans,maxValue(i+1,firstj,secondj,arr));
            if((arr[i][0].second!=firstj)&&(arr[i][0].second!=secondj))
            ans=max(ans,arr[i][0].first);
            if((arr[i][1].second!=firstj)&&(arr[i][1].second!=secondj))
            ans=max(ans,arr[i][1].first);
            if((arr[i][2].second!=firstj)&&(arr[i][2].second!=secondj))
            ans=max(ans,arr[i][2].first);
        }
        return dp[i][firstj+1][secondj+1]=ans;
    }
    long long maximumValueSum(vector<vector<int>>& board) {
        int n=board.size();
        int m=board[0].size();
        vector<vector<pair<long long,long long>>>arr;
        for(int i=0;i<n;i++){
            vector<pair<long long,long long>>temp;
            for(int j=0;j<m;j++){
                temp.push_back({board[i][j],j});
            }
            sort(temp.begin(), temp.end(), greater<pair<long long,long long>>());
            arr.push_back(temp);
        }
        cout<<arr.size()<<endl;
        for(int i=0;i<105;i++)for(int j=0;j<105;j++)for(int k=0;k<105;k++)dp[i][j][k]=-1;
        return maxValue(0,-1,-1,arr);
    }
};
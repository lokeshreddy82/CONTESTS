class solution:
     def build_a_matrix_with_conditions(self,k,row,col):
          from collections import defaultdict
          def dfs(node,adj,visited,order,has_cycle):
               visited[node] = True
               for neighbor in adj[node]:
                    if visited[neighbor]==0:
                         dfs(neighbor,adj,visited,order,has_cycle)
                         if has_cycle[0]:
                              return 
                    elif visited[neighbor]==1:
                         has_cycle[0] = True
                         return 
               visited[node]=2
               order.append(node)
          def topo(edges,n):
               adj=defaultdict(list)
               order=[]
               visited=[0]*(n+1)
               has_cycle=[False]
               for x,y in edges:
                    adj[x].append(y)
               for i in range(1,n+1):
                    if visited[i]==0:
                         dfs(i,adj,visited,order,has_cycle)
                         if has_cycle[0]:
                              return []
               order.reverse()
               return order
          order_r=topo(row,k)
          order_c=topo(col,k)
          if not order_r or not order_c:
               return []
          matrix=[[0]*k for _ in range(k)]
          pos_row={num:i for i,num in enumerate(order_r)}
          pos_col={num:i for i,num in enumerate(order_c)}
          for num in range(1,k+1):
               if num in pos_row and num in pos_col:
                    matrix[pos_row[num]][pos_col[num]]=num
          return matrix
s=solution()
k= 3
rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]
print(s.build_a_matrix_with_conditions(k,rowConditions,colConditions))
#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    
    #your code here
    
    def check(c,i):
        
        for j in range(V):
            if(graph[i][j]==1 and visit[j]==c):
                return False
        return True
        
        
    def back(i):
        if(i==V):
            return True
        
        for c in range(k):
            if(check(c,i)):
                visit[i]=c
                if(back(i+1)):
                    return True
                visit[i]=-1
        
        return False
    
    visit=[-1]*V
    return back(0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        V = int(input())
        k = int(input())
        m = int(input())
        l = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[l[cnt] - 1][l[cnt + 1] - 1] = 1
            graph[l[cnt + 1] - 1][l[cnt] - 1] = 1
            cnt += 2
        if (graphColoring(graph, k, V) == True):
            print(1)
        else:
            print(0)

        t = t - 1

# } Driver Code Ends
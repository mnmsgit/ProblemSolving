class Solution {
    public int solution(int n, int[][] computers) {
        int[] parent = new int[n];
        for (int i = 0 ;i < n; i++){
            parent[i] = i;
        }
        for (int i = 0; i < n; i++){
            int now_node = i;
            for (int j = 0; j < n; j++){
                if (computers[i][j] == 1){
                    union(i,j,parent);
                }
            }
        }
        int answer = 0;
        for(int i=0;i<n;i++){
            if (parent[i] ==i){
                answer +=1;
            }
        }
        
        return answer;
    }
    private int find_parent(int x,int[] parent){
        if (parent[x]== x){
            return x;
        }
        return find_parent(parent[x],parent);
         
    }
    private void union(int a, int b, int[] parent){
        a = find_parent(a,parent);
        b = find_parent(b,parent);
        if (a <= b){
            parent[b]= a;
        }
        else{
            parent[a] = b;
        }
    }
}
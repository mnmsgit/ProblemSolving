// System.out.println()
import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        List<String> myList = new ArrayList(Arrays.asList(words));
        myList.add(0,begin);
        int target_idx = -1;
        // start index가 begin인 graph
        int graphLen = words.length + 1;
        int[][] graph = new int[graphLen][graphLen];
        for(int i=0 ; i < graphLen;i++){
            if (myList.get(i).equals(target)){
                target_idx = i;
            }
            for(int j=0; j < graphLen; j++){
                graph[i][j] = getDistance(myList.get(i),myList.get(j));
                // System.out.print(graph[i][j]);
            }
            // System.out.println(myList.get(i)+"\n");
        }
        
        if (!myList.contains(target)){
            return 0;
        }
        answer = bfs(target_idx,graph);
        return answer;
    }
    private int getDistance(String word1, String word2){
        int distance = word1.length();
        for(int i =0; i< word1.length(); i++){
            if (word1.charAt(i) == word2.charAt(i)){
                distance -=1;
            }
        }
        return distance;
    }
    
    private int bfs(int target_idx, int[][] graph){
        Deque<Integer> queue = new LinkedList();
        queue.addFirst(0);
        int nowNode;
        int loopCount = graph[0].length;
        int[] distance = new int[loopCount]; 
        for (int i=0;i<loopCount; i++){
            distance[i] = 1000000;
        }
        
        distance[0] = 0;
        
        while (!queue.isEmpty()){
            nowNode = queue.remove();
            for(int j =0; j< loopCount; j++){
                if(graph[nowNode][j] == 1){
                    if (distance[nowNode]+1 < distance[j]){
                        distance[j] = distance[nowNode]+1;
                        queue.addFirst(j);
                    }
                }
            }
        }
        // for (int i=0; i<loopCount;i++){
        //     System.out.print(distance[i]);
        // }
        return distance[target_idx];
    }
}
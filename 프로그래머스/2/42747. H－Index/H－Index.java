import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Integer[] papers = new Integer[citations.length];
        for (int i =0; i<citations.length; i++){
            papers[i] = Integer.valueOf(citations[i]);
        }
        
        Arrays.sort(papers,Comparator.reverseOrder());
        for(int index = 0; index < papers.length; index++){
            int cadidate_num = Math.min(index+1,papers[index]);
            answer = Math.max(answer,cadidate_num);
        }
        
        return answer;
    }
    
}
import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        // int answer = 0;
        // return answer;
        List <Integer> prob_list = new ArrayList<>();
        // List <String> values_list = new ArrayList<>();
        HashMap<String, List <String>> colthesMap = new HashMap();
        for (int i=0;i<clothes.length; i++){
            String value = clothes[i][0];
            String key = clothes[i][1];
            if (colthesMap.containsKey(key)){
                List <String> values = colthesMap.get(key);
                values.add(value);
                colthesMap.put(key,values);
            }
            else{
                List <String> values = new ArrayList<>();
                values.add(value);
                colthesMap.put(key,values);
            }
        }
        for(String key:colthesMap.keySet()){
            List <String> tmp = colthesMap.get(key);
            prob_list.add(tmp.size()+1);
        }
        int ans = 1;
        for(Integer element:prob_list){
            ans = ans * element;
        }
        ans -=1;
        return ans;
    }   
}
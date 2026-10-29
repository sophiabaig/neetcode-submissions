class Solution {

    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> str_map = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {

            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String sorted_s = new String(chars);

            if (!str_map.containsKey(sorted_s)) {
                str_map.put(sorted_s, new ArrayList<>());
            }
    
            str_map.get(sorted_s).add(strs[i]);
        }
        return new ArrayList<>(str_map.values());
    }
}
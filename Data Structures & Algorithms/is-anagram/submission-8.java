class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> sCount = new HashMap<>();
        HashMap<Character, Integer> tCount = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {

            if (!sCount.containsKey(s.charAt(i))) {
                sCount.put(s.charAt(i), 0);
            }
            if (!tCount.containsKey(t.charAt(i))) {
                tCount.put(t.charAt(i), 0);
            }
            sCount.put(s.charAt(i), sCount.get(s.charAt(i)) + 1);
            tCount.put(t.charAt(i), tCount.get(t.charAt(i)) + 1);
        }

        return sCount.equals(tCount);
    }
}

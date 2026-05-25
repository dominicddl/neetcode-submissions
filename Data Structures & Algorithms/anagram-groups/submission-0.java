class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Initialise our hashmap to store key-value pairs
        // Each key-value pair is going to be a 26-length integer array
        // where each index from 0 to 25 corresponds to the letters 'a' to 'z'
        Map<String, List<String>> groupMap = new HashMap<>();

        // Iterate through our string array
        for (int i = 0; i < strs.length; i++) {
            int[] charFreq = new int[26];
            for (int j = 0; j < strs[i].length(); j++) {
                char c = strs[i].charAt(j);
                // Increment the count for each character in the string
                charFreq[c - 'a']++;
            }
            String key = Arrays.toString(charFreq);
            groupMap.computeIfAbsent(key, k -> new ArrayList<>()).add(strs[i]);
        }
        return new ArrayList<>(groupMap.values());
    }
}

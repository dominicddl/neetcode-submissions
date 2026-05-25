class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> seq = new HashSet<>();
        int longest = 0;
        for (int num : nums) {
            seq.add(num);
        }
        
        for (int num : seq) {
            if (!seq.contains(num - 1)) {
                int length = 1;
                while (seq.contains(num + length)) {
                    length++;
                }
                longest = Math.max(longest, length);
            }
        }
        return longest;
    }
}

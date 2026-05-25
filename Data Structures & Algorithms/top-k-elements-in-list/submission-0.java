class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Create an output array
        int[] res = new int[k];
        // Length of nums
        int len = nums.length;
        // Define a hashmap with key-value pair representing each number and its frequency
        Map<Integer, Integer> freqMap = new HashMap<>();
        // Define bucket (list of array lists)
        List<Integer>[] buckets = new ArrayList[len + 1];

        // Initialise buckets 
        for (int i = 0; i <= len; i++) {
            // each index is an array
            buckets[i] = new ArrayList<>();
        }

        // First pass: count frequencies
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Second pass: fill buckets
        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();
            buckets[freq].add(num);
        }

        // Iterate through the buckets and get the k most frequent
        int index = 0;
        for (int i = len; i >= 0 && index < k; i--) {
            for (int num : buckets[i]) {
                res[index++] = num;
                if (index == k) break;
            }
        }
        return res;
    }
}

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int len = numbers.length;
        int left = 0;
        int[] res = new int[2];
        while (left < len) {
            int right = left + 1;
            while (right < len) {
                if (numbers[left] + numbers[right] == target) {
                    res[0] = left + 1;
                    res[1] = right + 1;
                }
                right++;
            }
            left++;
        }
        return res;
    }
}

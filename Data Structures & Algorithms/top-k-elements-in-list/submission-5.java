class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        HashMap<Integer, Integer> counts = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (!counts.containsKey(nums[i])) {
                counts.put(nums[i], 0);
            }
            counts.put(nums[i], counts.get(nums[i]) + 1);
        }

        PriorityQueue<Integer> topK = new PriorityQueue<>((a, b) -> counts.get(a) - counts.get(b));

        for (int key : counts.keySet()) {

            topK.offer(key);

            if (topK.size() > k) {
                topK.poll();
            }
        }

        int[] output = new int[k];
        for (int i = 0; i < k; i++) {
            output[i] = topK.poll();
        }

        return output;
    }
}

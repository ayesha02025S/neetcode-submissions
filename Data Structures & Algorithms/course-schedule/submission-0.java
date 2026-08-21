class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();

        for(int i = 0; i< numCourses; i++) graph.add(new ArrayList<>());
        for(int [] p : prerequisites){
            int a = p[0], b = p[1];
            graph.get(b).add(a);
        }
            int [] state = new int[numCourses];

            for(int i = 0; i< numCourses; i++){
                if(state[i] == 0){
                    if(hasCycle(i, graph, state)) return false;
                }
            }
            return true;
        }
         private boolean hasCycle(int node, List<List<Integer>> g, int[] state) {
    state[node] = 1;                    // mark as visiting

    for (int next : g.get(node)) {      // check all edges node -> next
      if (state[next] == 1) return true;              // back edge means cycle
      if (state[next] == 0 && hasCycle(next, g, state)) return true;
    }

    state[node] = 2;                    // done exploring this node
    return false;
    }
}

int ans = 0;
void dfs(tree * T, int depth){
    if (T == NULL){
        ans = max(depth, ans);
        return;
    }
    dfs(T -> l, depth+1);
    dfs(T -> r, depth+1);

}
int solution(tree * T) {
    dfs(T, 0);
    return ans-1;
}
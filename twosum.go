func twoSum(nums []int, target int) []int {
    // start by creating a dict (find_index) that will contain the value
    // as the key and its index as the value
    // Then, for each value val in the list check if target - val 
    // exists in the dict. 
    //     If it does, return find_index[target - val ] and
    // the index of the current value
    //     If it does not, add find_index[target - val] = index of val
    // to the dict and continue
    
    find_index := make(map [int] int)
    out := make([]int, 2)
    for i, v := range(nums) {
        elem, ok := find_index[target - v];
        if !ok {
            find_index[v] = i
        } else {
            out[0] = elem
            out[1] = i
            break
        }
    }
    return out
}

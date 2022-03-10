class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char, int> seen;
        for (auto i : magazine) {
            std::map<char, int>::iterator it = seen.find(i);
            if (it == seen.end()) {
                seen[i] = 1;
            } else {
                it->second = it->second + 1;
            }
        }
        for (auto c : ransomNote) {
            std::map<char, int>::iterator check = seen.find(c);
            if (check == seen.end() or check->second == 0) {
                return false;
            } else {
                check->second = check->second - 1;
            }
            
        }
        return true;
    }
};

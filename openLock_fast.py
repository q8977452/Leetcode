class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        
        set1 = set(['0000'])
        set2 = set([target])
        
        def gen_node(node):
            new_nodes = [node[:i] + str((int(node[i]) + 1) % 10) + node[i+1:] for i in range(len(node))]
            new_nodes += [node[:i] + str((int(node[i]) - 1) % 10) + node[i+1:] for i in range(len(node))]
            return new_nodes
        
        cnt = 0
        while set1 and set2:
            cnt += 1
            if len(set1) > len(set2):
                set1, set2 = set2, set1
                
            curr = set()
            for node in set1:
                new_nodes = gen_node(node)
                for n in new_nodes:
                    if n in set2:
                        return cnt
                    if n in deadends:
                        continue
                    curr.add(n)
                    
            set1 = curr
                    
        return -1
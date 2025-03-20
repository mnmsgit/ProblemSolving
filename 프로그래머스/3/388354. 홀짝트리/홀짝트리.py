from collections import deque

def solution(nodes, edges):
    answer = [0, 0]
    # 그래프 생성 (양방향)
    graph = {node: [] for node in nodes}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # 연결 컴포넌트를 구한다. (한 번 계산한 결과를 재활용)
    visited = set()
    components = []  # 각 컴포넌트는 노드 리스트로 저장
    for node in nodes:
        if node not in visited:
            comp = []
            queue = deque([node])
            visited.add(node)
            while queue:
                cur = queue.popleft()
                comp.append(cur)
                for nxt in graph[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            components.append(comp)
    
    # 각 컴포넌트별로 홀짝트리 / 역홀짝트리 후보의 수를 계산한다.
    for comp in components:
        # 미리 각 노드의 차수(연결된 간선 수)를 구함
        degrees = {node: len(graph[node]) for node in comp}
        
        # [홀짝트리]
        # - 루트 노드: 조건은 (deg(root) % 2 == root % 2)
        # - 비루트 노드: 조건은 ((deg(node)-1) % 2 == node % 2)
        # 만약 비루트 조건을 위배하는 노드가 0개라면, 루트 조건만 맞는 노드가 후보
        # 만약 위배하는 노드가 1개라면, 오직 그 노드만 루트로 선택해야 전체 조건을 만족
        # 위배하는 노드가 2개 이상이면 어떤 루트를 선택해도 조건을 만족시킬 수 없다.
        bad_oetree = [v for v in comp if (degrees[v] - 1) % 2 != (v % 2)]
        if len(bad_oetree) == 0:
            count_oetree = sum(1 for v in comp if degrees[v] % 2 == (v % 2))
        elif len(bad_oetree) == 1:
            candidate = bad_oetree[0]
            count_oetree = 1 if degrees[candidate] % 2 == (candidate % 2) else 0
        else:
            count_oetree = 0
        answer[0] += count_oetree

        # [역홀짝트리]
        # - 루트 노드: 조건은 (deg(root) % 2 != root % 2)
        # - 비루트 노드: 조건은 ((deg(node)-1) % 2 != node % 2)
        bad_rev = [v for v in comp if (degrees[v] - 1) % 2 == (v % 2)]
        if len(bad_rev) == 0:
            count_rev = sum(1 for v in comp if degrees[v] % 2 != (v % 2))
        elif len(bad_rev) == 1:
            candidate = bad_rev[0]
            count_rev = 1 if degrees[candidate] % 2 != (candidate % 2) else 0
        else:
            count_rev = 0
        answer[1] += count_rev

    return answer

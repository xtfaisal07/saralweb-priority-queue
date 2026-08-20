from module import PriorityQueue

pq = PriorityQueue()

# Fresh start for testing
pq.repo.clear()
pq.heap.build_heap([])

a = pq.insert("Email Client", 30)
b = pq.insert("Deploy Backend", 5)
c = pq.insert("Fix UI Bug", 80)
d = pq.insert("Write Tests", 25)

print("\nInitial")
print(pq.display())

pq.update(c.id, 2)

print("\nAfter Update (80 → 2)")
print(pq.display())

pq.delete(d.id)

print("\nAfter Delete")
print(pq.display())

print("\nPeek")
print(pq.peek())

print("\nExtract Min")
print(pq.extract_min())

print("\nExtract Max")
print(pq.extract_max())

print("\nFinal")
print(pq.display())
class Node:
    def __init__(self, data): self.data, self.next = data, None

class LinkedListException(Exception): pass

class LinkedList:
    def __init__(self): self.head, self.size = None, 0

    def add(self, data):
        new_node = Node(data)
        if not self.head: self.head = new_node
        else:
            current = self.head
            while current.next: current = current.next
            current.next = new_node
        self.size += 1

    def print_list(self):
        if not self.head: print("List is empty")
        else:
            current, elements = self.head, []
            while current: elements.append(str(current.data)); current = current.next
            print(" -> ".join(elements))

    def delete_nth(self, n):
        if not self.head: raise LinkedListException("List is empty")
        if n < 1 or n > self.size: raise LinkedListException(f"Invalid index {n}")
        if n == 1: self.head = self.head.next
        else:
            current = self.head
            for _ in range(n - 2): current = current.next
            current.next = current.next.next
        self.size -= 1

    def get_nth(self, n):
        if not self.head or n < 1 or n > self.size: raise LinkedListException("Invalid index")
        current = self.head
        for _ in range(n - 1): current = current.next
        return current.data

    def is_empty(self): return self.head is None
    def get_size(self): return self.size
    def clear(self): self.head, self.size = None, 0

def menu(): print("\n".join([
    "1. Add element", "2. Display list", "3. Delete by position",
    "4. Get element by position", "5. Get list size",
    "6. Check if empty", "7. Clear list", "8. Exit"]))

def get_input(prompt, typ=str):
    while True:
        try: return typ(input(prompt))
        except ValueError: print(f"Enter valid {typ.__name__}")

def run():
    ll = LinkedList()
    print("Interactive Singly Linked List Program")
    while True:
        menu()
        choice = get_input("Enter choice (1-8): ", int)
        if choice == 1:
            data = input("Enter data: ")
            try: data = int(data)
            except: pass
            ll.add(data)
            print("Added:", data)
        elif choice == 2: ll.print_list()
        elif choice == 3:
            if ll.is_empty(): print("List is empty")
            else:
                pos = get_input(f"Enter position (1-{ll.get_size()}): ", int)
                try: ll.delete_nth(pos); print("Deleted position", pos)
                except Exception as e: print(e)
        elif choice == 4:
            if ll.is_empty(): print("List is empty")
            else:
                pos = get_input(f"Enter position (1-{ll.get_size()}): ", int)
                try: print("Element:", ll.get_nth(pos))
                except Exception as e: print(e)
        elif choice == 5: print("Size:", ll.get_size())
        elif choice == 6: print("Empty" if ll.is_empty() else "Not Empty")
        elif choice == 7:
            confirm = input("Clear list? (y/n): ").lower()
            if confirm in ['y', 'yes']: ll.clear(); print("List cleared")
        elif choice == 8:
            print("Final list:")
            ll.print_list()
            break
        else: print("Invalid choice!")
        input("Press Enter to continue...")

if __name__ == "__main__": run()
import sys
print(f"Python: {sys.version}")
try:
    from reme.memory.file_based_copaw import CoPawInMemoryMemory
    print("SUCCESS: CoPawInMemoryMemory imported")
except Exception as e:
    print(f"FAILED: {e}")

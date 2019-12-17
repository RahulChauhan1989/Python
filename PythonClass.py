class PythonClass:
    #print("Hello from class")
    articles="GlobalArticles"
    def __init__(self):
        print("Constructor")
    def displayName(self):
        print("Hello from {articles} class",self.articles)
      
a=PythonClass()
print(a.articles)
print(a.displayName())


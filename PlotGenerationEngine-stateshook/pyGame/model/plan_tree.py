#This file contains the functionality for creating the backend storage oobject for our
#generation engine. This structure is a general tree

#Class :  Task_Node
#This class creates the object that holds each task
class Task_Node():

    def __init__(self,task):
        self.__task = task
        self.__parent = None
        self.__children = []
        self.count = 0

    def add_child(self,child_node):
        self.__children.append(child_node)

    @property
    def task(self):
        return self.__task

    @property
    def parent(self):
        return self.__parent

    @property
    def children(self):
        return self.__children

    @property
    def count(self):
        return self.__count


 #This class hold all the functionality for building the Plan tree
class Plan_Tree():

    def __init__(self):
        self.__nodes = {}
        self.__root= None
        #NOTE: NEVER SUBTRACT FROM THIS NUMBER
        self.__count = 0

    @property
    def root(self):
        return self.__root

    @property
    def nodes(self):
        return self.__nodes

    @property
    def count(self):
        return self.__count


    #This function adds a task to the node
    #using a dictionary and a int value count to avoid collisions
    #Hooefully this makes it really fast
    def add_task(self,task,parent = None):
        self.count += 1
        print("Current Count: "+str(self.count))
        #Create new node object
        new_task_node = Task_Node(task)
        #set node index value to count of the tree
        new_task_node.count = self.count
        #add parent node if parent is not none
        if parent is not None:
            print("Made it here!!!!")
            print("Parent:" + ', ' .join(parent.task))
            new_task_node.parent = parent
            print("Parent:" + ', '.join(new_task_node.parent.task))
            # add the child node to the parents child list
            parent.add_child(new_task_node)

        #if no root node exists add root node
        if(self.root == None):
            self.root = new_task_node

        #Add node to dictionary
        self.nodes[self.count] = new_task_node

        return "Task Added!"


    def display_all(self):
        nodes_printed =0
        print("Display Muther Fuckin Tree!!")
        #Print the root node
        print ("ROOT NODE: " + ', ' .join(self.root.task) + " Count: " + str(self.root.count))
        nodes_printed +=1

        #If children exist print out all the children in a preorder manner
        if bool(self.root.children) != False:
            self.display_children(self.root)


    def display_children(self, current_node):
        #Go through child array printing all children if they exist
        for child in current_node.children:
            print ("Task: " + ', '.join(child.task) + " Parent: " + ', ' .join(child.parent.task) + "Count: " +str(child.count))
            #if Children are found in child array of child, print before next child of parent
            if bool(child.children)!= False:
                self.display_children(child)










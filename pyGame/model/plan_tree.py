#This file contains the functionality for creating the backend storage oobject for our
#generation engine. This structure is a general tree

#Class :  Task_Node
#This class creates the object that holds each task

class Task_Node():

    def __init__(self,task):
        self.__task = task
        self.__parent = None
        self.__children = []
        self.__count = 0

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
    def count(self,value):
        self.__count = value


    def get_node(self,count):
        return self.__nodes[count]

    #This function adds a task to the node
    #using a dictionary and a int value count to avoid collisions
    #Hooefully this makes it really fast
    def add_task(self,task,parent = None):
        self.__count +=1
        #print("Current Count: "+str(self.__count))
        #Create new node object
        new_task_node = Task_Node(task)
        #set node index value to count of the tree
        new_task_node.__count = self.__count
        #add parent node if parent is not none
        if parent is not None:
            #Set parent to the parent of the new task node
            new_task_node.__parent = parent
            print("Parent:" + ', '.join(new_task_node.__parent.task))
            # add the child node to the parents child list
            parent.add_child(new_task_node)

        #if no root node exists add root node
        if(self.__root == None):
            self.__root = new_task_node

        #Add node to dictionary
        self.__nodes[self.__count] = new_task_node

        return "Task Added!"


    def display_all(self):
        nodes_printed =0
    #    print("Display Muther Fuckin Tree!!")
        #Print the root node
        print ("ROOT NODE: " + ', ' .join(self.__root.task) + " Count: " + str(self.__root.__count))
        nodes_printed +=1

        #If children exist print out all the children in a preorder manner
        if bool(self.root.children) != False:
            self.display_children(self.root)


    def display_children(self, current_node):
        #Go through child array printing all children if they exist
        for child in current_node.children:
            print ("Task: " + ', '.join(child.task) + " Parent: " + ', ' .join(child.__parent.task) + " Count: " +str(child.__count))
            #if Children are found in child array of child, print before next child of parent
            if bool(child.children)!= False:
                self.display_children(child)


    #returns a list of plans
    def get_plan(self,node):
        #Create a empty list called plan
        plan = []
        # if the node has no parents just return that singular task
        if node.__parent is None:
            print('Here!!')
            plan.append(node.task)
            return plan
        #if parents of the node do exist
        if node.__parent is not None:
            plan = self.get_parent_task(node.__parent,plan)
            # Add the task of the current node to the list
            plan.append(node.task)
            return plan

    def get_parent_task(self, node, plan):
        if node is not None:
            if node.__count != self.__root.__count:
                plan = self.get_parent_task(node.__parent,plan)
            plan.append(node.task)
        return plan

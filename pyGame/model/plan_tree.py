#This file contains the functionality for creating the backend storage oobject for our
#generation engine. This structure is a general tree

#Class :  Task_Node
#This class creates the object that holds each task. You create each node object by passing it the task value held in
#that nodde
#In each node object it holds the following values
#Value: tesk = List that holds the task set to that node
#Value: parent = holds a reference to the parent node of the current node
#Value: children = A list that hold references to all the children if this node
#Value: count = int value that is the unique indentifer of this node, this values never changes and is set by the plan tree
#               object the node is stored in
#Value: depth = a reference to which level the of the tree the node is stored in, this value is set by the plane, tree
#               and is based off of the parent depth the node is set as the child of
# REMARK; The following are values that are to be used with the GUI, this is part of partial feature and we are not sure if this is
# the correct place to put these values
#Value: x = hold the x coordinate box for drawing in the GUI
#Value y = homy the y coordinate box for drawing the GUI
class Task_Node():

    def __init__(self,task):
        self.task = task
        self.parent = None
        self.children = []
        self.count = 0
        self.depth = 0
        self.x = 0
        self.y = 0

    def add_child(self,child_node):
        self.children.append(child_node)

#Class : Plan_Tree
#Descrption: This class hold all the functionality for building the Plan tree. The Plan Tree data structure is a general
#tree.
#value : nodes =  list of all the node object in the tree
#value : root =  reference to the node object in the tree that is the root of the tree
#value : node_count = the number of nodes created in this tree, this is used as the unique idemtifier for each node,
#        this value should be incremented every time a new node object is created
#value : max_depth = hold the depth value of the tree
#REMARK - the following values have to due with the partially implemented GUI feature, not sure if this is the permanent
#location for these values or if they may be moved somewhere else in the future
#value : x_max = holds the max width of the GUI
#value : y_max = holds the max height of the GUI
class Plan_Tree():

    def __init__(self):
        self.nodes = {}
        self.root= None
        #NOTE: NEVER SUBTRACT FROM THIS NUMBER
        self.node_count = 0
        self.max_depth = 0
        self.x_max = 500
        self.y_max = 500
    #Method: get_node - pass in the unqiue identifer for the node in nodes and it will return which node you requested
    # returns the node object request based on the unique identifer called count
    def get_node(self,count):
        return self.nodes[count]

    #Method: add_task - This function adds a task to the node
    #param : task - the task itself being passed to the node, ex. ('stack', 'b', 'a')
    #param : parent - if parent exists pass a refernce to parent object to the function
    #using a dictionary and a int value count to avoid collisions
    def add_task(self,task,parent = None):
        self.node_count += 1
        #Create new node object
        new_task_node = Task_Node(task)
        #set node index value to count of the tree
        new_task_node.count = self.node_count
        #add parent node if parent is not none
        if parent is not None:
            #Set parent to the parent of the new task node
            new_task_node.parent = parent
            # add the child node to the parents child list
            parent.add_child(new_task_node)
            #give child correct depth
            new_depth = parent.depth +1
            new_task_node.depth = new_depth
            if new_depth > self.max_depth:
                self.max_depth = new_depth
        #if no root node exists add root node
        if(self.root == None):
            self.root = new_task_node

        #Add node to dictionary
        self.nodes[self.node_count] = new_task_node
        #Return text on success
        return "Task Added!"

    #Method : display_all - print out all nodes in preorder depth first fashion
    #root has a special print out then the rest of the nodes are printed out in the following fashion
    # Task: ... Parent: ... Count: ....
    def display_all(self):
        #count the number of nodes printed
        nodes_printed =0

        #Print the root node
        print ("ROOT NODE: " + ', ' .join(self.root.task) + " Count: " + str(self.root.count))
        nodes_printed +=1

        #If children exist print out all the children in a preorder manner
        if bool(self.root.children) != False:
            self.display_children(self.root)

    #Mothod: display_children - helper function used to help display_all, used to recurisvly call printing the children
    # and the children of those children
    def display_children(self, current_node):
        #Go through child array printing all children if they exist
        for child in current_node.children:
            print ("Task: " + ', '.join(child.task) + " Parent: " + ', ' .join(child.parent.task) + " Count: " +str(child.count))
            #if Children are found in child array of child, print before next child of parent
            if bool(child.children)!= False:
                self.display_children(child)


    #Methos: get_plan - based on the node input to the function the function call all the from the selected node to the root
    # of the tree and then combines all the tasks from the root node to the node input into the function to generate a plane
    #value : node -  reference to the node object you want to generate a plan to
    def get_plan(self,node):
        #Create a empty list called plan
        plan = []
        # if the node has no parents just return that singular task
        if node.parent is None:
            #print('Here!!')
            plan.append(node.task)
            return plan
        #if parents of the node do exist
        if node.parent is not None:
            plan = self.get_parent_task(node.parent,plan)
            # Add the task of the current node to the list
            plan.append(node.task)
            return plan

    #Method : get_parent_task - helper function to support recursive call to root from the selected node in get_plan,
    #param : node - the node being checked for a parent and append its task to the plan
    #param : plan - the plan passed to each function to continue building the plan
    def get_parent_task(self, node, plan):
        #get the plan of the parent if not non
        if node is not None:
            #if we are not at root get the next parent until root is reached
            if node.count != self.root.count:
                #call the next parent recursively
                plan = self.get_parent_task(node.parent,plan)
            plan.append(node.task)
        #return the plan
        return plan

#NOTE - The functionality beyond this point was for an incomplete feature, it is up to whoever takes this if they want to
# continue it or not

    #Method : get_depth_count - Returns a count of nodes available at a given depth level designated by the variable level
    #param : level - the depth you want to count the number of nodes at
    def get_depth_count(self,level):
        count = 0
        for node in self.nodes:
            if node.depth == level:
                count += 1

        return count

    #Method get_subtree_width- finds the max width of each subtree so we know how to space the nodes for the GUI
    #param : subroot - the root for each subtree
    def get_subtree_width(self,subRoot):
        #Max Width is always one becuase of root node
        max_width = 1
        depth_count=[0] * 100
        depth = 0
        #set root depth depth
        depth_count[depth] = 1
        depth +=1
        #get next level depth
        depth_count[depth] = len(subRoot.children)
        depth += 1
        #get depth for rest of levels
        if len(self.root.children ) > 0:
            #Do somthing

            for child in subRoot.children:
                depth_count = self.get_subtree_width_helper(child,depth_count,depth)

            #Return max width

            for width in depth_count:
                if(width > max_width):
                    max_width = width

        # return the max width
        return max_width

    def get_subtree_width_helper(self,currentNode,depth_count,depth):
        # get depth for rest of levels
        if len(currentNode.children) > 0:
            # Do somthing
            depth_count[depth] = len(currentNode.children)
            depth+=1
            for child in currentNode.children:
                depth_count = self.get_subtree_width_helper(child, depth_count, depth)
        return depth_count


    def generate_x_Y_coordinates(self,pane_width,pane_height,box_width,box_height):
        localx = 250
        localy = 0
        total_width = 0
        #horizontal box padding
        h_box_padding = 10
        #vertical box padding
        v_box_padding = 50
        calc_pane_width = 0
        calc_pane_height = 0
        #Set Coordinates for root
        self.root.x = localx
        self.root.y = localy
        subtree_pixels = [0] * len(self.root.childrem)
        #get to total width for the tree
        for child in self.root.children:
            total_width += self.getsubtree_width(child)
        calc_pane_width = ((box_width+h_box_padding)*total_width)+h_box_padding
        calc_pane_height =((box_height+v_box_padding)*self.max_depth)+v_box_padding

        #distrbute pixels to each subtree
        child_count = 0
        for child in self.root.children:
            child_width = self.getsubtree_width(child)
            ratio = child_width / total_width
            subtree_pixels[child_count] = (int)(ratio * calc_pane_width)
            child_count += 1

        #set the left and right bounds for each subtree
        subtree_left_bounds = [0] * len(self.root.children)
        subtree_right_bounds = [0] * len(self.root.children)
        child_count = 0
        for child in self.root.children:
            if(child_count == 0):
                subtree_left_bounds[child_count] = 0
                subtree_right_bounds[child_count] = subtree_pixels[child_count]- 1

            else:
                subtree_left_bounds[child_count] = subtree_right_bounds[child_count-1] -1
                subtree_right_bounds[child_count] = subtree_left_bounds[child_count] + subtree_pixels[child_count] - 1

            child_count +=1



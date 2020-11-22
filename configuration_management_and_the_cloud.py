# Summary:
    # Site Reliability Engineer
    # Configuration Management
    # Puppet
        # Resources
        # Facts
        # Manifests
            # Module
        # Catalog
        # Declaring and referring resources
        # Node
            # Node definitions
        # Puppet parser validate
        # rspec tests
    # Scale
    # Unmanaged configuration
    # A list of Configuration Management Systems
    # Infrastructure as Code (IaC)
    # Domain-Specific Language (DSL)
    # Production
    # Cloud
        # Software as a Service (SaaS)
        # Platform as a Service (PaaS)
        # Infrastructure as a Service (IaaS)
        # Regions
        # Capacity
        # Scaling
            # Horizontal scaling
            # Vertical scaling
            # Automatic scaling
            # Manual scaling
        # Containers
        # Types of clouds:
            # Public clouds
            # Private clouds
            # Hybrid clouds
            # Multi-clouds
    # Reference images
    # Templating
    # Disk image
    
    
# ==============================================================================
# Site Reliability Engineer:
    # A team that is focused on the reliability and maintainability of large system. They apply tons of automation techniques to manage them.
# ==============================================================================
# Configuration Management:
    # An automation technique which lets us manage the configuration of our computers at scale.
    # Operations should be idempotent:
        # An idempotent action can be performed over and over again without changing the system after the first time the action was performed and with no unintended side effects.
# ==============================================================================
# Puppet:
    # The current industry standard for configuration management.
    # Puppet uses a declarative language as opposed to procedural languages like Python.
    
    # Resources:
        # The basic unit for modeling the configuration that we want to manage.

    # Facts:
        # Variables that represent the caracteristics of the system.
        # For example, what the current OS is, how much memory the computer has, whether it's a virtual machine or not, what the current IP address is.
        
    # Manifests:
        # Files that end with a .pp extension.
        # A file that stores the rules that we want to apply. These files are stored in a directory called 'manifests'.
        # The first manifest that puppet reads is called 'init.pp'.
        
        # Module:
            # A collection of manifests and associated data.
        
    # Catalog:
        # The list of rules that are generated for one specific computer once the server has evaluated all variables, conditionals, and functions.
        
    # Declaring and referring resources:
        # We write resource types in lowercase when declaring them, but capitalize them when referring to them from another resource's attribute.
        
    # Node:
        # Any system where we can run a Puppet agent.
        
        # Node definitions:
            # These are files that are stored with the name 'site.pp' which isn't part of any module. Instead, it just defines what classes will be included for what nodes.
            
    # Puppet parser validate:
        # Checks that the syntax of the manifests is correct.
        
    # rspec tests:
        # Test manifests automatically. In these tests we can set the facts involved different values and check that the catalog ends up stating what we wanted it to.
# ==============================================================================
# Scale:
    # Being able to scale what we do means that we can keep achieving large impacts with the same amount of effort.
    # A scalable system is a flexible one.
# ==============================================================================
# Unmanaged configuration:
    # Manually deploying the installation and configuring the computer.
# ==============================================================================
# A list of Configuration Management Systems:
    # Puppet
    # Chef
    # Ansible
    # CFEngine
# ==============================================================================
# Infrastructure as Code (IaC):
    # When all the configuration necessary to deploy and manage a node in the infrastructure is stored in version control.
# ==============================================================================
# Domain-Specific Language (DSL):
    # A programming language that's more limited in scope. Unlike General Purpose Languages like Python, Ruby, Java or Go.
# ==============================================================================
# Production:
    # The parts of the infrastructure where as service is executed and served to its users.
# ==============================================================================
# Cloud:
    # A service that's running somewhere else. Either in the datacenter or other remote servers that we can reach over the internet.
    
    # Software as a Service (SaaS):
        # When a Cloud provider delivers an entire application or program to the cusomer.
        
    # Platform as a Service (PaaS):
        # When a Cloud provider offers a preconfigured platform to the customer.
        
    # Infrastructure as a Service (IaaS):
        # When a Cloud provider supplies only the bare-bones computing experience.
        # Some IaaS products are:
            # Amazon's EC2
            # Google Compute Engine
            # Microsoft Azure Compute
            
    # Regions:
        # A geographical location containing a number of data centers, regions contain zones and zones can contain one or more physical data centers.
        # Large cloud providers usually offer their services in lots of different regions around the world. Generally, the region and zone you select should be closest to your users, the farther your users are from the physical data center, the more latency they may experience.
        
    # Capacity:
        # How much the service can deliver.
        
    # Scaling:
        # Changing the capacity. Upscaling and downscaling.
        
        # Horizontal scaling:
            # We add more nodes into the pool that's part of a specific service.
            # For example, you add more servers to increase the capacity.
            
        # Vertical scaling:
            # Here you make your nodes bigger instead of adding more nodes.
            # When we say bigger here, we're talking about the resources assigned to the nodes like memories, CPU, and disk space.
            # For example, a database server with a 100 gb of disk space can store more data than with only 10 gb of space. To scale this deployment we can just add a bigger disk to the machine and the same idea works for a CPU and memory too.
            
        # Automatic scaling:
            # The service offered by the Cloud provider will use metrics to automatically increase or decrease the capacity of the system.
            
        # Manual scaling:
            # Changes are controlled by humans instead of software.
            # When the Cloud deployment isn't very complex, it's usually easier for smaller organizations to user manual scaling practices.
            
    # Containers:
        # Applications that are packaged together with their configuration and dependancies.
        
    # Types of clouds:
        # Public clouds:
            # The cloud service provided to you by a third party. It's called public because Cloud providers offer services to the public. Like Microsoft Azure.
        # Private clouds:
            # When your company owns the services and the rest of your infrastructure, whether that's on-site or in a remote data center. Like Chimply.
        # Hybrid clouds:
            # A mixture of both public and private clouds.
        # Multi-clouds:
            # A mixture of public and/or private clouds across vendors.
# ==============================================================================
# Reference images:
    # Store the contents of a machine in a reusable format.
# ==============================================================================
# Templating:
    # The process of capturing all of the system configuration to let us create VMs in a repeatable way.
# ==============================================================================
# Disk image:
    # A snapshot of a virtual machine's disk at a given point in time.
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
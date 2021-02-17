from urllib.request import urlretrieve
from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server
from diagrams.programming.language import Bash
from diagrams.generic.storage import Storage
from diagrams.azure.database import BlobStorage
from diagrams.custom import Custom
from diagrams.azure.integration import APIManagement
from diagrams.azure.analytics import EventHubs
from diagrams.azure.compute import FunctionApps
from diagrams.azure.database import CosmosDb
# Download an image to be used into a Custom Node class

#pbi_url = "https://www.rippedorange.co.nz/wp-content/uploads/2019/08/power-bi-icon-15.png"

# pbi_icon = "./pbi.png"

# urlretrieve(pbi_url)


with Diagram("Workflow  \n ", show=True):

    with Cluster("On-premise"):

        on_premise = [

            Server("unix_st server")

            - Storage("Daily reports (csv/txt) \n from 20+ scratch disks")

            >> Bash("Scheduled \n bash script (cron job) \n via azcopy sync \n command")]

    with Cluster("Azure"):

        azure = BlobStorage("Blob Storage \n Container")

    # with Cluster("Power BI Service"):

        # pbi = Custom("Daily report \n on disk usage", pbi_icon)

    on_premise >> azure

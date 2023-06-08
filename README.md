# Militarization of Police
A web app and data project by the Stanford Know Systemic Racism Project, with partners American Friends Service Committee (AFSC) and Electronic Frontier Foundation (EFF)

Developed by Tracy Wei

*This web app is still a working prototype.*

![research poster](https://ibb.co/mJMgkgJ])

## tl;dr
California State Assembly Bill 481 (AB-481), which became effective January, 2022, requires law enforcement agencies to post annual reports about the military equipment that they own. But what exactly is this military equipment and what is it used for?

According to AB-481, "The public has a right to know about any funding, acquisition, or use of military equipment by state or local government officials, as well as a right to participate in any government agency’s decision to fund, acquire, or use such equipment." This web app is intended to make it easier for the public to understand. The purpose of the project is also to help people understand how military equipment may influence change police culture.

In this project, we want to look at data on military equipment cost, the relationship between equipment and deaths/injury, and information found in the policy manuals of California law enforcement agencies. We intend to make the data readily available as interactive visualizations for legislators and activists. 

## Link to demo
https://goto.stanford.edu/militarization (Hosted on Streamlit server, as of 5/16/2023) 

## More about this project:
As a research assistant for Know Systemic Racism, I built a wireframe and coded a web-based application that makes the military equipment inventory of California law enforcement agencies visible to legislators and citizens. My work directly contributes to a project with the Electronic Frontier Foundation and American Friends Service Committee that shows the militarization of police using law enforcement records of military equipment. 

My initial task involved designing a wireframe in Figma for the web application, which would be used as a foundation for the rest of the project. This wireframe included a map view page for users to filter and select specific law enforcement agencies to learn more details about their respective inventories. It also included a gallery view of military equipment that filters inventory by where the user lives so that users can learn more about the military equipment in their local law enforcement agencies and how much money is being put towards those. After a few rounds of iteration with feedback from the team, the wireframe was complete.

Before I started building out the wireframe, I helped gather data on the military equipment of law enforcement agencies, examining policy manuals to record their equipment and respective costs. 

The main task of this project was to build the web application, which was developed using Streamlit and the programming language Python since the Streamlit framework supports data-driven web applications. I used our dataset containing the equipment list to create a table view, which is a modified version of the gallery view from the wireframe that showcases all the equipment and their details like manufacturer, cost, etc. along with images of each equipment. To help users look for specific categories of military equipment and certain companies, I added in dropdown menus that allow the user to filter the inventory based on the criteria they want to look at and a search bar to search for certain equipment. Using the Plotly library, I also built a map view of California, its counties colored by population, and its law enforcement agencies as points on the map. We wanted to show the data and military inventory of these law enforcement agencies on an individual level. Thus, I coded the map to allow these law enforcement agencies to be selected on the map and then show the data we collected on that selected law enforcement agency, including its inventory.

Our next steps are to create data visualizations for the quantity and cost of military equipment for both individual and all law enforcement agencies and aggregate by categories of equipment, manufacturers, and county. 

# Route-Optimization-Around-Island-Using-Genetic-Algorithm
> This note record and share the final project of [GA course](https://timetable.nycu.edu.tw/?r=main/crsoutline&Acy=112&Sem=2&CrsNo=517408&lang=zh-tw) about developing an optimized route planning system for customized needs and deploying the result on website.

# Project Overview

## 1. Research Background and Purpose

### 1.1 Background and Motivation
We planned a budget-friendly 11-day motorcycle trip around Taiwan, aiming to calculate the optimal route that balances cost efficiency and enjoyment. The journey starts from National Chiao Tung University, traveling counterclockwise around Taiwan, focusing on scenic spots without considering accommodation or meals.

### 1.2 Literature Review
- **Factors Affecting Travel Quality:**  
  Huang (2007) identified three main factors: travel characteristics (attraction count, duration), route characteristics (distance, transport mode), and destination characteristics (stay time, attraction info). With the internet, travelers can customize trips based on these factors.
- **Multi-Day Travel Planning:**  
  Two methods: City model (filters out non-selected cities) and Central Point model (selects attractions within a radius from a central point).  
  Wang (2014) suggested decision factors like daily travel distance/time limits, combined into a linear function for optimization.
- **Traveling Salesman Problem (TSP):**  
  The TSP seeks the shortest route visiting each city once and returning to the start. Metaheuristic algorithms like Genetic Algorithms (GA) offer near-optimal solutions efficiently, which we will use in this project.

### 1.3 Objective
We aim to calculate the optimal route using Google Maps API and a Genetic Algorithm, considering:
- **Attraction Rating:** Prioritizing higher-rated attractions.
- **Distance:** Minimizing actual riding distance.
- **Central Attractions:** Selecting attractions near major roads or of personal interest.

**Selected Central Attractions:**
- **Hsinchu:** Hsinchu City East District Roundabout
- **Miaoli:** Miaoli Gongguan
- **Taichung:** Fengyuan Mazu Temple, Taichung Park
- **Nantou:** Caotun Town Office
- **Yunlin:** Gukeng Green Tunnel
- **Chiayi:** Southern Branch of the National Palace Museum
- **Tainan:** Qigu Salt Mountain, Yuguang Island
- **Kaohsiung:** Kōshan's Eye, Cijin Old Street
- **Pingtung:** Kenting National Park
- **Taitung:** Duoliang Station, Brown Avenue
- **Hualien:** Baxian Cave, Pacific Park
- **Yilan:** Qingshui Geothermal Park, Bambi Hills
- **New Taipei:** Wenshan Caotang, Shiding Crocodile Island
- **Taipei:** Rongjin Time Living Park, National Palace Museum
- **Taoyuan:** Senlin Riverside Café, Daxi Old Street

## 2. Research Methodology

### 2.1 Building the Attraction Database
- **Central Points:** Google Maps API is used to find central attraction coordinates.
- **Nearby Attractions:** Using Google Maps API, we locate the top 10 high-rated attractions within a small radius, with at least 100 reviews.

### 2.2 Generating Distance Matrix
Using Google Maps API, we calculate distances between attractions, storing them in a 10x10 matrix for the TSP optimization, saved as a .txt file.

### 2.3 Optimal Route Generation
We use the following fitness function:
value = rating * 1 - total_distance

Rating is weighted higher than distance (1 vs. -1). The algorithm generates one route, which may have a reverse option, but we focus on a counterclockwise direction, favoring north-to-south paths along the west coast. Each county's "local optimal route" is combined to form the final "Best Round-the-Island Route."

### 2.4 Full Route Optimization
All data is consolidated into a single CSV file, removing initial restrictions for a more flexible, globally optimized route.

## 3. Research Results

### 1. Scenic Spot Itinerary
We planned a route starting from NCTU, traveling counterclockwise through Miaoli, Taichung, and Nantou, and finally back to Taipei. The spots are as follows:

**Starting point:** NCTU  
**Miaoli:** Maoli Mountain Park ⮕ Gongweixu Tunnel ⮕ Golden Town Leisure Farm  
**Taichung:** Lihpao Metasequoia Road ⮕ Dakeng No. 8 Hiking Trail ⮕ Green Sky Railway 1908  
**Nantou:** Nantou Lantern Festival Water Plaza ⮕ Zhongxing New Village Parent-Child Park  
**Yunlin:** Douliu Seed Park ⮕ Taiping Old Street  
**Chiayi:** Puzi River Cycling Path ⮕ Hebao Islet Ecological Park  
**Tainan:** Hollyhock Flower Festival ⮕ Chihkan Cultural Park ⮕ Barkley Memorial Park  
**Kaohsiung:** Gangshan Park ⮕ Pier-2 Art Center  
**Pingtung:** Shuangliu Waterfall Trail ⮕ Taiwan’s Southernmost Point ⮕ Longpan Park  
**Taitung:** South Cross-Island Highway ⮕ Taimali Level Crossing ⮕ Water Flows Uphill  
**Hualien:** Fuli Flower Fields ⮕ Pacific Park  
**Yilan:** Bambi Hills ⮕ Luodong Forestry Culture Garden  
**New Taipei:** Yin-Yang Sea ⮕ Jinguashi Geological Park ⮕ Golden Waterfall  
**Taipei:** Rongjin Life Park ⮕ National Palace Museum  
**Taoyuan:** Sky Rope Bridge ⮕ Daxi Zhongzheng Park ⮕ Daxi Riverside Park  
**Hsinchu:** Lee Kecheng Residence ⮕ Chenghuang Temple Plaza ⮕ Hsinchu Park ⮕ Back to NCTU

### 2. Scooter Riding Path
The riding path between the above spots was mapped using MyMap, and due to the genetic algorithm rules, some scenic spots are distributed around a center point.

### 3. Website Display
Using Vue.js, we successfully built a website. You can access it via the QR Code below. The website includes features such as zooming and switching between satellite and terrain views.

### 4. Route Comparison Analysis
Here’s a comparison between our route and a blog from the internet:

| Metric           | Our Method - GA    | Blog Route (also counterclockwise) |
| ---------------- | ------------------ | ---------------------------------- |
| Total distance    | 1360.9 km          | 1218 km                            |
| Riding difficulty | 123.718 km/day     | 150-200 km/day                     |
| Days              | 11 days            | 9 days                             |
| Number of spots   | 74                 | 42                                 |

## 5. Feasibility Analysis
We analyzed the feasibility from three aspects and believe this route is viable:
- **Riding Distance:** Daily riding distance is moderate
- **Spot Ratings:** The selected spots have good reviews and high ratings
- **Personal Needs:** Flexible adjustment of lodging and meal times

## 4. Conclusion and Future Outlook

In this project, we implemented a genetic algorithm to plan a round-island route based on personal preferences and distances, with the results displayed on the website. Two areas for future optimization:
1. **Algorithm:** Adjust parameters, optimize starting point settings
2. **Website:** Add more detailed route planning between spots

## 5. References
1. Ying-Cheng Huang (2005), "A Study on Recreational Route Planning Models", Master's Thesis, Chaoyang University of Technology.
2. Guang-Sheng Li (2009), "Application of Genetic Algorithms in Hualien City Travel Itinerary Optimization", Master's Thesis, National Dong Hwa University.
3. You-Cheng Chen (2008), "A Travel Itinerary Planning System Based on Travel Pushing Algorithms", Master's Thesis, Tamkang University.
4. Chi-An Lu (2009), "Tourism Planning System with Accommodation and Interest Spots Considerations", Master's Thesis, Tamkang University.
5. Yu-Ting Wang (2010), "Application of Genetic Algorithms in Multi-day Travel Itinerary Planning", Master's Thesis, Chang Jung Christian University.


<!--
## Feature
1. User Capabilities:
    -  Account Management: Users can register, login, and manage their accounts.  
    -  Account Management: Users can register, login, and manage their accounts.  
    - Vehicle Booking: Browse available vehicles(at least two types of vehicles), book rentals, and manage bookings(cancel order).
    - Payment System: Process payments for rentals(at least three payment methods) and receive invoices.
    - Review and Ratings: Rate vehicles and provide feedback on rental experiences.
      
2. System Manager Capabilities:
    - Vehicle Management: Add, update, and remove vehicles from the system.
    - Booking Management: View and manage all bookings, check vehicle availability.
    - Customer Service: Handle customer inquiries and manage disputes.
    - Financial Overviews: Track payments, generate revenue reports, and manage pricing models.
3. Six locations(manager can add and delete sites)
4. Fool-proof design
5. Bouns :
     - Dynamic Pricing Model: Implement a dynamic pricing model that changes based on demand, season, and type of vehicle.



## ER diagram 
<div align="center"><img src="https://imgur.com/eCBybwd.png" width="400" height="400"></div>

## Web
👉 Click [Figma](https://www.figma.com/proto/m1CDNRBHq86n3vmHeBlPmv/carSharing?node-id=0-1&t=EZrLlnQJwGSpKPAv-1) to see full design
1. Customer
    - Homepage/ Order page/ QnA page

<div align="center">
    <img src="https://imgur.com/L2q2zwm.png" width="220" height="220">
    <img src="https://imgur.com/DDu3LdP.png" width="192" height="220">
    <img src="https://imgur.com/ZjCybnx.png" width="248" height="220">
</div>
<br>

2. Order car page
    - Admin Homepage/ Station management page/ Reply page

<div align="center">
    <img src="https://imgur.com/qMoJUTM.png" width="240" height="160">
    <img src="https://imgur.com/qEujLFA.png" width="240" height="160">
    <img src="https://imgur.com/0GrMDfM.png" width="244" height="160">
</div>-->
<br><br>

👨‍🏫 Advicing Professor : CHUN-CHENG LIN<br>
👧 Team members : WAN-CHIN TSAI, HSIN-YI PAI, CHIH-CHUN CHANG, CHING-CHUN LAI

###### tags:  `Genetic Algorithm` `Google API` `Python` `Vue` `HTML` `CSS` `JS` `Visual Studio`


> 🔍 Watch MORE ➜ [My GitHub](https://github.com/iriszzzz)

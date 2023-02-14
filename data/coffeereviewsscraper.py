Python project for scraping coffee reviews from ttps://www.coffeereview.com for data analysis




(venv) $ python -m pip install requests
(venv) $ python -m pip install beautifulsoup4

import requests
import pandas as pd
from bs4 import BeautifulSoup

coffee_reviews_URL = https://www.coffeereview.com/review/page/

# create lists for all the features we want to capture
rating = []
roaster = []
title = []
roaster-location = []
coffee-origin = []
roast-level = []
agtron = []
price = []
review-date = []
aroma = []
acidity = []
body = []
flavor = []
aftertaste = []
blind-assessment = []
notes = []
bottom-line = []


# maybe start with just 1 page...
# Scrape all reviews, from pages 1 to 353
for x in range(1, 353):
	URL = coffee_reviews_URL + str(x)
	review_page = requests.get(URL)

	# creates a soup object that helps parse the html
	soup = BeautifulSoup(review_page.content, "html.parser")
	main_content = soup.find(id="genesis-content")

	# get each review on the page
	review_elements = main_content.find_all("div", class_="entry-content")

	# for each review, follow the link to the full review page
	for review_element in review_elements:

		# get the link the to full review
		last_row = review_element.find_all("div", class_="row row-3")
		link = last_row.find("a")
		link_url = link["href"]

		# go the the full review page and extract info
		single_review_page = requests.get(link_url)
		sub_soup = BeautifulSoup(single_review_page.content, "html.parser")
		review_content = sub_soup.find("div", class_="review_template")
		
		# extract data from elements
		rating.append(review_content.find("span", class_="review-template-rating").text)
		roaster.append(review_content.find("p", class_="review-roaster").text)
		title.append(review_content.find("h1", class_="review-title").text)
		
		# extract data from tables
		table_data = []

		tables = review_content.find_all("table", class_="review-template-table")
		for table in tables:
			table_body = table.find("tbody")

			table_rows = table_body.find_all("tr")
			for table_row in table_rows:
				table_cols = table_row.find_all("td")

				# the data is stored in the 2nd column, the 1st column is only the label
				data.append(table_cols[1])
		
		roaster-location.append(table_data[0].text)
		coffee-origin.append(table_data[1].text)
		roast-level.append(table_data[2].text)
		agtron.append(table_data[3].text)
		price.append(table_data[4].text)
		review-date.append(table_data[5].text)
		aroma.append(table_data[6].text)
		acidity.append(table_data[7].text)
		body.append(table_data[8].text)
		flavor.append(table_data[9].text)
		aftertaste.append(table_data[10].text)

		# extract data from paragraphs to get the blind assessment, notes and bottom line
		paragraphs = review_content.find_all("p")
			
		blind-assessment.append(paragraphs[-5].text)
		notes.append(paragraphs[-4].text)
		bottom-line.append(paragraphs[-3].text)

# TODO
# maths (price per ounce)
# conversions (convert date format to numeric values)
# type conversions from string to int



dict = {"rating": rating, "roaster"; roaster, "title": title, "roaster-location": roaster-location, "coffee-origin": coffee-origin, 
 "roast-level": roast-level, "agtron": agtron, "price": price, "review-date": review-date, "aroma": aroma, "acidity": acidity,
 "body": body, "flavor": flavor, "aftertaste": aftertaste, "blind-assessment": blind-assessment, "notes": notes, "bottom-line": bottom-line}

coffee_reviews_df = pd.DataFrame(dict) 
coffee_reviews_df.to_csv('GFG.csv')










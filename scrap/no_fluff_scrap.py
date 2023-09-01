import datetime
import unicodedata

from helper.help import get_selenium_driver, get_config, get_dom, to_csv


def processing_jobs(groups):
    """Getting data from groups"""
    main_list = []

    for group in groups:
        title_of_group = group.select_one("div").find("h2").text.strip()
        items = group.find_all("a", class_='posting-list-item')
        for item in items:
            group_dict = {}
            title_job = item.select_one("div>div>h3").text.strip()
            company = item.find("span", class_="d-block posting-title__company text-truncate").text.strip()
            salary = item.find("span", class_="text-truncate badgy salary tw-btn tw-btn-secondary-outline tw-btn-xs "
                                              "ng-star-inserted").text.strip()
            city = item.find("span", class_="tw-text-ellipsis tw-inline-block tw-overflow-hidden tw-whitespace-nowrap "
                                            "lg:tw-max-w-[100px] tw-text-right").text.strip()

            group_dict['title_of_group'] = title_of_group
            group_dict['title_job'] = title_job
            group_dict['company'] = company
            group_dict['salary'] = unicodedata.normalize('NFKC', salary)
            group_dict['city'] = city

            main_list.append(group_dict)

    return main_list


if __name__ == "__main__":
    browser = get_selenium_driver()
    CONFIG = get_config()
    dom = get_dom(url=CONFIG['scraper']['url']['MasterUrl'], browser=browser)
    tables = dom.find_all("nfj-postings-list")

    received_data = processing_jobs(tables)

    filename = (CONFIG['scraper']['url']['MasterUrl'] + "_" + str(datetime.datetime.now())).replace("https://", "")\
                   .replace("/", "_") + ".csv"

    to_csv(received_data, filename)

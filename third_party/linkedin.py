from dotenv import load_dotenv
import os
import requests


load_dotenv()
def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from linkedin profile
    Manually scrape infomation from linkedin profile
    """
    api_endpoint = f"https://nubela.co/proxycurl/api/v2/linkedin?url={linkedin_profile_url}&fallback_to_cache=on-error&use_cache=if-present"
    header_dic = {
        "Accept": "application/json",
        "Authorization": f"Bearer {os.getenv('PROXYCURL_API_KEY')}",
    }

    # print(api_endpoint)
    # print(header_dic)
    payload = {}
    response = requests.request("GET", api_endpoint, headers=header_dic, data=payload)

    data = response.json()
    # print(data)
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
import requests
from decouple import config

url = config("RAPID_API_CURRENCY_URL")
api_key = config("RAPID_API_CURRENCY_KEY")
api_host = config("RAPID_API_CURRENCY_HOST")

headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": api_host
}

currencies_codes = {
"AED":"UAE Dirham",
"AFN":"Afghan Afghani",
"ALL":"Albanian Lek",
"AMD":"Armenian Dram",
"ANG":"Netherlands Antillean Gulden",
"AOA":"Angolan Kwanza",
"ARS":"Argentine Peso",
"AUD":"Australian Dollar",
"AWG":"Aruban Florin",
"AZN":"Azerbaijani Manat",
"BAM":"Bosnia And Herzegovina Konvertibilna Marka",
"BBD":"Barbadian Dollar",
"BDT":"Bangladeshi Taka",
"BGN":"Bulgarian Lev",
"BHD":"Bahraini Dinar",
"BIF":"Burundi Franc",
"BMD":"Bermudan Dollar",
"BND":"Brunei Dollar",
"BOB":"Bolivian Boliviano",
"BRL":"Brazilian Real",
"BSD":"Bahamian Dollar",
"BTC":"Bitcoin",
"BTN":"Bhutanese Ngultrum",
"BWP":"Botswana Pula",
"BYN":"New Belarusian Ruble",
"BYR":"Belarusian Ruble",
"BZD":"Belize Dollar",
"CAD":"Canadian Dollar",
"CDF":"Congolese Franc",
"CHF":"Swiss Franc",
"CLF":"Chilean Unit Of Account",
"CLP":"Chilean Peso",
"CNY":"Chinese Yuan",
"COP":"Colombian Peso",
"CRC":"Costa Rican Colon",
"CUC":"Cuban Convertible Peso",
"CUP":"Cuban Peso",
"CVE":"Cape Verdean Escudo",
"CZK":"Czech Koruna",
"DJF":"Djiboutian Franc",
"DKK":"Danish Krone",
"DOP":"Dominican Peso",
"DZD":"Algerian Dinar",
"EGP":"Egyptian Pound",
"ERN":"Eritrean Nakfa",
"ETB":"Ethiopian Birr",
"EUR":"Euro",
"FJD":"Fijian Dollar",
"FKP":"Falkland Islands Pound",
"GBP":"British Pound",
"GEL":"Georgian Lari",
"GGP":"Guernsey Pound",
"GHS":"Ghanaian Cedi",
"GIP":"Gibraltar Pound",
"GMD":"Gambian Dalasi",
"GNF":"Guinean Franc",
"GTQ":"Guatemalan Quetzal",
"GYD":"Guyanese Dollar",
"HKD":"Hong Kong Dollar",
"HNL":"Honduran Lempira",
"HRK":"Croatian Kuna",
"HTG":"Haitian Gourde",
"HUF":"Hungarian Forint",
"IDR":"Indonesian Rupiah",
"ILS":"Israeli New Sheqel",
"IMP":"Manx pound",
"INR":"Indian Rupee",
"IQD":"Iraqi Dinar",
"IRR":"Iranian Rial",
"ISK":"Icelandic Kr\xc3\xb3na",
"JEP":"Jersey Pound",
"JMD":"Jamaican Dollar",
"JOD":"Jordanian Dinar",
"JPY":"Japanese Yen",
"KES":"Kenyan Shilling",
"KGS":"Kyrgyzstani Som",
"KHR":"Cambodian Riel",
"KMF":"Comorian Franc",
"KPW":"North Korean Won",
"KRW":"South Korean Won",
"KWD":"Kuwaiti Dinar",
"KYD":"Cayman Islands Dollar",
"KZT":"Kazakhstani Tenge",
"LAK":"Lao Kip",
"LBP":"Lebanese Lira",
"LKR":"Sri Lankan Rupee",
"LRD":"Liberian Dollar",
"LSL":"Lesotho Loti",
"LVL":"Latvian Lats",
"LYD":"Libyan Dinar",
"MAD":"Moroccan Dirham",
"MDL":"Moldovan Leu",
"MGA":"Malagasy Ariary",
"MKD":"Macedonian Denar",
"MMK":"Myanma Kyat",
"MNT":"Mongolian Tugrik",
"MOP":"Macanese Pataca",
"MRO":"Mauritanian Ouguiya",
"MUR":"Mauritian Rupee",
"MVR":"Maldivian Rufiyaa",
"MWK":"Malawian Kwacha",
"MXN":"Mexican Peso",
"MYR":"Malaysian Ringgit",
"MZN":"Mozambican Metical",
"NAD":"Namibian Dollar",
"NGN":"Nigerian Naira",
"NIO":"Nicaraguan Cordoba",
"NOK":"Norwegian Krone",
"NPR":"Nepalese Rupee",
"NZD":"New Zealand Dollar",
"OMR":"Omani Rial",
"PAB":"Panamanian Balboa",
"PEN":"Peruvian Nuevo Sol",
"PGK":"Papua New Guinean Kina",
"PHP":"Philippine Peso",
"PKR":"Pakistani Rupee",
"PLN":"Polish Zloty",
"PYG":"Paraguayan Guarani",
"QAR":"Qatari Riyal",
"RON":"Romanian Leu",
"RSD":"Serbian Dinar",
"RUB":"Russian Ruble",
"RWF":"Rwandan Franc",
"SAR":"Saudi Riyal",
"SBD":"Solomon Islands Dollar",
"SCR":"Seychellois Rupee",
"SDG":"Sudanese Pound",
"SEK":"Swedish Krona",
"SGD":"Singapore Dollar",
"SHP":"Saint Helena Pound",
"SLL":"Sierra Leonean Leone",
"SOS":"Somali Shilling",
"SRD":"Surinamese Dollar",
"STD":"Sao Tome And Principe Dobra",
"SVC":"Salvadoran Col\xc3\xb3n",
"SYP":"Syrian Pound",
"SZL":"Swazi Lilangeni",
"THB":"Thai Baht",
"TJS":"Tajikistani Somoni",
"TMT":"Turkmenistan Manat",
"TND":"Tunisian Dinar",
"TOP":"Paanga",
"TRY":"Turkish New Lira",
"TTD":"Trinidad and Tobago Dollar",
"TWD":"New Taiwan Dollar",
"TZS":"Tanzanian Shilling",
"UAH":"Ukrainian Hryvnia",
"UGX":"Ugandan Shilling",
"USD":"United States Dollar",
"UYU":"Uruguayan Peso",
"UZS":"Uzbekistani Som",
"VEF":"Venezuelan Bolivar",
"VND":"Vietnamese Dong",
"VUV":"Vanuatu Vatu",
"WST":"Samoan Tala",
"XAF":"Central African CFA Franc",
"XAG":"Silver (troy ounce)",
"XCD":"East Caribbean Dollar",
"XDR":"Special Drawing Rights",
"XOF":"West African CFA Franc",
"XPF":"CFP Franc",
"YER":"Yemeni Rial",
"ZAR":"South African Rand",
"ZMK":"Old Zambian Kwacha",
"ZMW":"Zambian Kwacha",
"ZWL":"Zimbabwean Dollar"
}

async def currency_converter(have:str, want:str, amount:float):

  print(have, want, amount)

  querystring = {"have":have,"want":want,"amount":amount}

  response = requests.get(url, headers=headers, params=querystring)
  
  response_json = response.json()
  
  return response_json
**Navigation:** [← Previous](./20-set-environment-variables-for-api-keys.md) | [Index](./index.md) | [Next →](./22-pulumi.md)

# Integrations
Source: https://docs.pinecone.io/integrations/overview

Pinecone integrations enable you to build and deploy AI applications faster and more efficiently. Integrate Pinecone with your favorite frameworks, data sources, and infrastructure providers.

export const OpenAIIcon = () => <svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
    <g id="Group 1">
      <path id="image 20 (Traced)" fill-rule="evenodd" clip-rule="evenodd" d="M13.4979 0.429336C10.9373 0.983683 8.71757 2.74598 7.56566 5.139C7.1015 6.10324 7.09344 6.11087 6.28596 6.34639C4.50122 6.86705 2.62234 8.36513 1.61101 10.0739C-0.128538 13.0127 0.0682218 16.7915 2.10117 19.4925C2.5581 20.0996 2.5631 20.122 2.39916 20.8032C2.18307 21.7008 2.16347 23.5698 2.36036 24.5045C2.53557 25.3364 3.29535 27.0663 3.73476 27.6335C4.42849 28.5293 5.53785 29.5332 6.37718 30.0246C7.96363 30.9533 10.1655 31.4212 11.7307 31.1621C12.4218 31.0476 12.4303 31.0508 13.1381 31.6859C13.9676 32.4303 15.4388 33.2334 16.528 33.5361C20.6551 34.6836 25.055 32.5382 26.6886 28.5819C26.8908 28.0925 27.0051 28.0093 27.9465 27.6672C30.559 26.7176 32.3301 24.9354 33.2342 22.3461C33.5686 21.3882 33.628 21.0006 33.6297 19.7631C33.6323 17.6853 33.1778 16.2284 32.0214 14.6075L31.5571 13.9566L31.7575 13.0134C32.1499 11.1672 31.9096 9.40479 31.0147 7.56487C30.2988 6.09326 28.6691 4.46141 27.2312 3.77649C25.7186 3.05593 24.5231 2.8096 22.9267 2.88931L21.6079 2.95515L20.9104 2.34189C18.9858 0.650021 16.0171 -0.116 13.4979 0.429336ZM17.2733 2.78021C18.2881 3.12788 19.4046 3.84621 19.159 3.99343C19.0503 4.05858 17.491 4.95491 15.6937 5.98514C13.8964 7.01551 12.3008 7.98115 12.1479 8.13114C11.8819 8.39216 11.8679 8.61534 11.8298 13.2521C11.8079 15.9185 11.7552 18.1001 11.7126 18.1001C11.6701 18.1001 11.0481 17.7727 10.3303 17.3723L9.02529 16.6446L9.02223 12.1864C9.0189 7.22719 9.08523 6.75643 9.98559 5.35774C11.5156 2.9808 14.6368 1.87682 17.2733 2.78021ZM25.5632 5.46905C27.2766 6.1239 28.6961 7.52605 29.315 9.17537C29.6384 10.0369 29.8416 11.8431 29.6524 12.1736C29.5503 12.3519 28.9275 12.0372 25.9836 10.3205C23.16 8.67398 22.3609 8.26657 22.0601 8.32022C21.8523 8.35737 20.1003 9.30013 18.1666 10.4153C16.2329 11.5304 14.3849 12.5956 14.0598 12.7822L13.4689 13.1214V11.4647V9.80804L16.8409 7.87344C20.8895 5.55056 20.9193 5.53517 21.844 5.27568C22.8311 4.99871 24.5693 5.08909 25.5632 5.46905ZM7.03781 17.1577C7.13362 17.2727 9.05686 18.4204 11.3117 19.7086C13.5668 20.9969 15.412 22.082 15.4123 22.1201C15.4125 22.1582 14.783 22.5468 14.0132 22.9836L12.6138 23.7776L9.12193 21.7636C5.17854 19.4891 4.80352 19.2372 4.08795 18.3834C2.43893 16.4158 2.17431 13.693 3.41188 11.4263C3.91803 10.4992 5.10206 9.33395 5.98254 8.89633L6.72481 8.52759L6.79433 12.7382C6.84523 15.8187 6.91058 17.0051 7.03781 17.1577ZM25.117 12.382C29.2405 14.754 30.0398 15.3921 30.7776 16.9017C31.0438 17.4465 31.3245 18.2965 31.4012 18.7908C31.7885 21.2857 30.4399 23.9729 28.2047 25.1606L27.3741 25.6019V21.4617C27.3741 18.1284 27.3362 17.2695 27.1792 17.0554C27.0718 16.9093 25.1534 15.7277 22.9158 14.4298C20.6783 13.132 18.8506 12.0113 18.8542 11.9393C18.8608 11.8125 21.2062 10.3719 21.4439 10.3488C21.5092 10.3424 23.1621 11.2575 25.117 12.382ZM18.8395 13.8631L20.6301 14.8938L20.6682 17.0168L20.7063 19.1397L18.9648 20.1448C18.007 20.6976 17.1571 21.1498 17.0762 21.1498C16.9951 21.1498 16.1488 20.7002 15.1955 20.1509L13.462 19.1521L13.5003 17.0184L13.5384 14.8848L15.2765 13.8642C16.2325 13.3031 17.0223 12.8413 17.0318 12.8382C17.0411 12.8351 17.8546 13.2963 18.8395 13.8631ZM23.5739 16.5881C24.2492 16.9764 24.8799 17.3583 24.9755 17.4368C25.2057 17.6259 25.2219 25.5048 24.9942 26.5839C24.5459 28.7088 23.0166 30.463 20.9082 31.2706C19.7319 31.7212 17.9092 31.7205 16.7366 31.269C15.7965 30.907 14.8317 30.3171 14.9274 30.1626C14.9623 30.1064 16.4817 29.2102 18.304 28.1711C20.1263 27.132 21.7549 26.154 21.9231 25.9976C22.2274 25.7151 22.2292 25.6842 22.2292 20.7978C22.2292 18.0941 22.2556 15.8821 22.2877 15.8821C22.32 15.8821 22.8987 16.1999 23.5739 16.5881ZM20.6953 22.6399L20.6911 24.2687L17.1892 26.2722C15.2631 27.3741 13.3409 28.413 12.9175 28.5808C9.9169 29.7699 6.45671 28.3644 5.03421 25.3784C4.59563 24.4578 4.52082 24.1487 4.46117 23.0119C4.42349 22.2927 4.43253 21.7042 4.48147 21.7042C4.53042 21.7042 5.96252 22.5066 7.66397 23.4872C11.4365 25.6615 11.5583 25.7243 12.0056 25.7243C12.32 25.7243 14.0128 24.7976 19.2395 21.7643C19.9278 21.3648 20.538 21.0319 20.5953 21.0246C20.6526 21.0171 20.6976 21.744 20.6953 22.6399Z" fill="var(--text-primary)" />
    </g>
  </svg>;

export const SagemakerIcon = () => <svg width="50" height="50" viewBox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg">
    <g id="square logos">
      <path id="image 24 (Traced)" fill-rule="evenodd" clip-rule="evenodd" d="M22.9874 10.0114L24.9928 11.2228L27.1076 9.98679L29.2222 8.75059L33.0116 11.276L36.8008 13.8012L36.8052 16.1506L36.8098 18.5L38.9052 19.7654L41.0008 21.031V25.2V29.3692L39.3508 30.2436L37.7008 31.118L37.6008 33.791L37.5008 36.464L34.7008 38.2342C33.1608 39.2078 31.2938 40.3734 30.552 40.8244L29.2034 41.6444L27.1084 40.4046L25.0136 39.1646L22.9978 40.3824C21.8892 41.052 20.9188 41.5976 20.8414 41.5946C20.7642 41.5916 18.8558 40.4342 16.6008 39.0228L12.5008 36.4564L12.4008 33.8182L12.3008 31.1798L10.6008 30.2342L8.90077 29.2886L8.84677 25.1882L8.79297 21.0878L10.9968 19.8202L13.2008 18.5526V15.9192V13.2856L16.9508 11.0504C19.0134 9.82099 20.7642 8.81179 20.8414 8.80759C20.9188 8.80339 21.8846 9.34519 22.9874 10.0114ZM19.5238 10.6298L18.2008 11.4222V14.211V17H17.7008H17.2008V14.5044V12.0086L15.7008 12.9192L14.2008 13.83V16.2088V18.5878L15.6894 19.5922L17.1778 20.5966L18.7894 19.571L20.4008 18.5452V16.9726C20.4008 15.5334 20.4348 15.4 20.8008 15.4C21.1726 15.4 21.2008 15.5334 21.2008 17.285V19.1698L19.4008 20.3108L17.6008 21.452V23.0234V24.5948L19.0928 25.8194L20.5848 27.044L20.6428 28.5398L20.7008 30.0358L22.6508 28.4842C24.573 26.9548 24.6008 26.9204 24.6008 26.0752C24.6008 25.2264 24.5868 25.2096 23.2048 24.3884C21.9836 23.663 21.834 23.5116 22.0118 23.1796C22.1234 22.9708 22.2792 22.8066 22.3578 22.8146C22.4364 22.8228 23.1308 23.209 23.9008 23.6732L25.3008 24.517L25.3546 28.9586L25.4084 33.4H27.0892C28.7042 33.4 28.7944 33.3756 29.3934 32.7766C29.9198 32.2504 30.1168 32.1732 30.6582 32.2814C32.113 32.5724 32.6106 34.1962 31.5296 35.126C30.7526 35.7944 29.8998 35.7482 29.2008 35C28.6668 34.4284 28.5632 34.4 27.0134 34.4H25.3864L25.4436 36.3488L25.5008 38.2976L27.3616 39.4286L29.2224 40.5596L32.9116 38.2316L36.6008 35.9038V33.2628V30.6218L37.9982 29.8876C38.7666 29.4836 39.3478 29.076 39.2894 28.9814C39.231 28.887 38.6042 28.486 37.8966 28.0902C36.6982 27.42 36.5632 27.3878 35.926 27.6182C34.7306 28.0504 33.6008 27.252 33.6008 25.9752C33.6008 25.752 33.8744 25.2956 34.2088 24.9612C34.7158 24.4542 34.9214 24.3742 35.4456 24.479C36.2834 24.6466 36.7668 25.1152 36.9146 25.9034C36.9868 26.2876 37.2124 26.6384 37.4686 26.7638C37.7062 26.8804 38.3734 27.253 38.9508 27.592L40.0008 28.208L39.9944 24.854L39.988 21.5L37.9944 20.3018L36.0008 19.1036V18.0518V17H35.2584C34.7044 17 34.4122 17.1286 34.1084 17.5064C33.1122 18.744 31.1208 18.0876 31.1208 16.5214C31.1208 15.6494 31.6282 15.0646 32.5434 14.8814C33.0848 14.7732 33.2818 14.8504 33.8082 15.3766C34.2942 15.8626 34.6046 16 35.2162 16C35.9978 16 36.0008 15.997 36.0008 15.203V14.4058L32.7052 12.203C30.8926 10.9914 29.311 9.99999 29.1904 9.99999C29.07 9.99999 28.166 10.4698 27.1816 11.044L25.392 12.0878L25.4464 15.5716L25.5008 19.0554L27.3178 20.2006C29.0664 21.3026 29.1556 21.3348 29.6876 21.0562C30.764 20.4922 32.0008 21.269 32.0008 22.509C32.0008 23.4252 31.2676 24.2 30.4008 24.2C29.6426 24.2 28.8008 23.4228 28.8008 22.7226C28.8008 22.3076 28.4618 22.0222 26.7112 20.9636L24.6214 19.7L24.5612 15.8422L24.5008 11.9842L22.6738 10.911L20.8466 9.83759L19.5238 10.6298ZM32.2168 16.0808C31.8062 16.5756 32.142 17.234 32.768 17.1616C33.213 17.1102 33.3008 17.0012 33.3008 16.5C33.3008 16.044 33.2006 15.8856 32.8832 15.8404C32.6536 15.8076 32.3538 15.9158 32.2168 16.0808ZM11.6508 20.5214L9.80077 21.6242V22.9104V24.1968L11.3092 23.4504C12.5896 22.8168 12.8462 22.749 13.0062 23.002C13.1098 23.1658 13.1956 23.345 13.1966 23.4C13.1976 23.455 12.4346 23.905 11.5008 24.4L9.80317 25.3L9.80197 27.0278L9.80077 28.7554L11.3654 29.5694L12.9298 30.3834L14.2388 29.5052C15.2136 28.8514 15.6058 28.685 15.7744 28.8536C16.1782 29.2574 16.0138 29.486 14.6966 30.3512L13.4008 31.2026V33.554V35.9054L15.5682 37.2528C16.7604 37.9938 17.8266 38.6 17.9378 38.6C18.0488 38.6 18.9154 38.015 19.8632 37.3C20.8112 36.585 21.6704 36 21.7724 36C21.9256 36 22.2008 36.4488 22.2008 36.6984C22.2008 36.7346 21.4408 37.327 20.512 38.0148L18.8234 39.2656L19.8404 39.9068L20.8572 40.548L22.5218 39.5532C23.4374 39.006 24.2812 38.4442 24.3972 38.3044C24.5356 38.1376 24.5896 36.366 24.5544 33.1448L24.5008 28.239L21.0262 31.0196C19.1152 32.5488 17.5208 33.8 17.4832 33.8C17.4456 33.8 17.3204 33.6236 17.2052 33.408C17.0224 33.0666 17.1632 32.8816 18.298 31.9722L19.6008 30.9282V29.1812V27.434L18.5508 26.5942C17.9734 26.1324 17.3948 25.7126 17.2652 25.6614C17.1358 25.6102 16.3428 26.0318 15.503 26.5984C14.2698 27.4306 13.921 27.5828 13.6886 27.3898C13.5302 27.2584 13.4008 27.0856 13.4008 27.0056C13.4008 26.9256 14.1658 26.351 15.1008 25.7288L16.8008 24.5974V23.024V21.4504L15.2392 20.4252C14.3804 19.8614 13.6378 19.4042 13.5892 19.4094C13.5406 19.4146 12.6684 19.915 11.6508 20.5214ZM29.7868 22.1168C29.5968 22.3458 29.5818 22.526 29.7328 22.7668C30.2388 23.574 31.4536 23.0462 31.0076 22.2128C30.7448 21.7216 30.1534 21.6752 29.7868 22.1168ZM34.6776 25.6884C34.4624 26.2492 34.6962 26.699 35.2354 26.7616C35.8532 26.8334 36.1954 26.1756 35.7928 25.6904C35.4828 25.317 34.8206 25.3158 34.6776 25.6884ZM29.8776 33.4884C29.6624 34.0492 29.8962 34.499 30.4354 34.5616C31.0532 34.6334 31.3954 33.9756 30.9928 33.4904C30.6828 33.117 30.0206 33.1158 29.8776 33.4884Z" fill="var(--text-primary)" />
    </g>
  </svg>;

export const BedrockIcon = () => <svg width="50" height="50" viewBox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg">
    <g id="square logos">
      <path id="image 23 (Traced)" fill-rule="evenodd" clip-rule="evenodd" d="M16.9959 11.051L12.7226 13.4922L12.6803 16.203L12.6381 18.9136L10.6189 20.0579L8.59961 21.2022L8.6411 25.2556L8.68243 29.3092L10.6598 30.7151L12.637 32.1211L12.641 34.3794L12.6449 36.6377L16.8492 39.1188C19.1614 40.4835 21.0774 41.6 21.1069 41.6C21.1363 41.6 22.1451 41.0755 23.3486 40.4345L25.5368 39.2691L25.5396 35.6563L25.5424 32.0434H27.8732H30.2041L30.2036 33.2477L30.2033 34.452L29.6257 34.7628C28.781 35.2173 28.3393 35.9594 28.34 36.9224C28.3419 39.4601 31.3545 40.2656 32.8032 38.1158C33.5728 36.974 32.9883 35.2468 31.6415 34.6837C31.3089 34.5444 31.2919 34.4538 31.2919 32.8243V31.1111H28.4171H25.5424V29.4795V27.8479H29.4744H33.4064L33.8723 28.3529C34.7137 29.2649 34.7175 29.2757 34.4612 30.0198C34.1647 30.88 34.2971 31.7424 34.8213 32.3652C35.9314 33.6843 37.7466 33.5891 38.8084 32.1561C39.039 31.8448 39.1281 31.489 39.1281 30.878C39.1281 29.9239 38.8378 29.4089 37.9594 28.804C37.5019 28.4888 37.2968 28.4495 36.453 28.5146L35.4761 28.59L34.7437 27.7546L34.0112 26.9194L29.7768 26.9175L25.5424 26.9155V25.517V24.1185H31.04H36.5374L36.7344 24.5941C36.8429 24.8556 37.1781 25.2578 37.4794 25.4876C37.9274 25.8293 38.1901 25.9055 38.9214 25.9055C39.8755 25.9055 40.3891 25.646 40.9667 24.8724C41.694 23.8983 41.3174 22.1509 40.2363 21.4827C39.6244 21.1045 38.4706 21.0618 37.829 21.3935C37.312 21.661 36.5752 22.4931 36.5752 22.8096C36.5752 22.9967 35.7264 23.0307 31.0588 23.0307H25.5424V21.3991V19.7675H29.2718H33.0012V17.8419C33.0012 15.9694 33.0109 15.914 33.354 15.8279C34.2774 15.5962 35.1628 14.0836 34.9479 13.1053C34.6739 11.8579 33.4174 10.948 32.1955 11.1119C29.8849 11.4218 29.3333 14.7018 31.4291 15.6689L32.0607 15.9604L32.0648 17.3201L32.0688 18.6798H28.8082H25.5477L25.5062 14.7732L25.4647 10.8667L23.4446 9.72862C22.3335 9.10255 21.3895 8.59473 21.3468 8.60002C21.3041 8.6053 19.3462 9.70827 16.9959 11.051ZM22.9736 10.6383L24.4514 11.4541L24.4141 20.3063L24.3769 29.1583L20.5288 31.1987C18.4124 32.3208 16.6442 33.2757 16.5995 33.3204C16.4365 33.4833 16.8963 34.2307 17.1091 34.1491C17.2265 34.1041 18.8986 33.2272 20.825 32.2007C22.7514 31.174 24.3561 30.3341 24.3911 30.3341C24.426 30.3341 24.4546 32.2103 24.4546 34.5036V38.6729L22.8244 39.5538C21.9278 40.0381 21.1639 40.4345 21.1269 40.4345C21.09 40.4345 20.4569 40.0742 19.72 39.634L18.3804 38.8332L19.3586 38.2179C19.8965 37.8794 20.366 37.5753 20.4017 37.5421C20.4957 37.4546 20.0737 36.7052 19.9304 36.7052C19.8639 36.7052 19.2674 37.0525 18.6048 37.477L17.4 38.249L16.6831 37.8266C16.2888 37.5945 15.4295 37.0897 14.7736 36.7052L13.5811 36.0059L13.5847 34.0635L13.5884 32.1211L15.2922 30.9681C16.2292 30.3341 16.9959 29.7878 16.9959 29.7542C16.9959 29.7208 16.8745 29.5323 16.7261 29.3356L16.4562 28.9779L14.8665 30.0445C13.9922 30.6311 13.2049 31.1111 13.117 31.1111C13.029 31.1111 12.2226 30.582 11.3249 29.9354L9.69248 28.7595L9.69791 27.2549L9.7032 25.7501L11.328 24.8177C12.2216 24.3049 12.9534 23.8406 12.9541 23.7861C12.9551 23.7314 12.8289 23.53 12.6738 23.3386L12.3918 22.9903L11.7803 23.3689C11.4439 23.5769 10.8366 23.9387 10.4306 24.1725L9.69248 24.5977L9.69698 23.1538L9.70164 21.7099L11.436 20.753L13.1703 19.7963L14.8888 20.7086L16.6074 21.6209L16.6523 22.8589L16.6974 24.097L15.7199 24.9122C14.7195 25.7468 14.6673 25.8637 15.087 26.3297C15.3136 26.5813 15.3876 26.548 16.2372 25.8119L17.1453 25.0252L18.3947 25.9058L19.6442 26.7862L19.9373 26.4243C20.0984 26.2253 20.1999 26.013 20.1624 25.9526C20.1251 25.8923 19.5345 25.4482 18.85 24.9657L17.6053 24.0885L17.6502 22.8216L17.6951 21.5545L19.676 20.5445L21.657 19.5344L21.6573 17.4755L21.6576 15.4166H21.1137H20.5699L20.5664 17.1647L20.5632 18.9129L18.8579 19.8059L17.1527 20.6988L15.3611 19.8071L13.5698 18.9153L13.6124 16.5248L13.655 14.1343L14.9758 13.3814C15.7022 12.9673 16.3468 12.6265 16.408 12.624C16.4694 12.6215 16.5393 13.4063 16.5634 14.3677L16.6074 16.1158H17.0736H17.5397L17.6174 13.9776L17.6951 11.8395L19.4821 10.8344C20.465 10.2815 21.3201 9.82776 21.3824 9.8259C21.4447 9.82403 22.1608 10.1895 22.9736 10.6383ZM33.5312 12.6315C34.0762 13.279 34.0583 13.917 33.4793 14.4962C32.8686 15.1069 32.2014 15.1069 31.5907 14.4962C30.6732 13.5788 31.2522 12.1533 32.5423 12.1533C33.0066 12.1533 33.2128 12.2531 33.5312 12.6315ZM39.8503 22.5526C40.7849 23.4873 40.2298 24.8954 38.9268 24.8954C38.4311 24.8954 38.2343 24.8028 37.9098 24.4173C36.7462 23.0346 38.575 21.2773 39.8503 22.5526ZM37.267 29.6216C37.8637 29.871 38.1291 30.2679 38.1291 30.9109C38.1291 31.8646 37.1242 32.555 36.2582 32.1963C35.0483 31.695 34.9888 30.1379 36.1601 29.6283C36.7708 29.3626 36.6487 29.3634 37.267 29.6216ZM31.7192 36.0144C32.3905 36.7773 31.9905 38.1191 31.0373 38.3012C30.1533 38.4702 29.2604 37.7629 29.2772 36.9072C29.3019 35.6575 30.8933 35.0757 31.7192 36.0144Z" fill="var(--text-primary)" />
    </g>
  </svg>;

<CardGroup cols={3}>
  <style jsx>
    {`
        .integration-logo img {
          width: 50px;
          height: 50px;
          object-fit: contain;
        }`}
  </style>

  <Card href="/integrations/ai-engine">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/YhGPIXwx2i0D3QjI/images/integrations/ai-engine.png?fit=max&auto=format&n=YhGPIXwx2i0D3QjI&q=85&s=17778f9229c5046988b3ff604c7c6a81" data-og-width="100" width="100" data-og-height="100" height="100" data-path="images/integrations/ai-engine.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/YhGPIXwx2i0D3QjI/images/integrations/ai-engine.png?w=280&fit=max&auto=format&n=YhGPIXwx2i0D3QjI&q=85&s=abf1ec165b75bbaa9047ec754b60ad2c 280w, https://mintcdn.com/pinecone/YhGPIXwx2i0D3QjI/images/integrations/ai-engine.png?w=560&fit=max&auto=format&n=YhGPIXwx2i0D3QjI&q=85&s=9139bcae82a017f7b0e5246ff42156a4 560w, https://mintcdn.com/pinecone/YhGPIXwx2i0D3QjI/images/integrations/ai-engine.png?w=840&fit=max&auto=format&n=YhGPIXwx2i0D3QjI&q=85&s=afaa4dea8e8e31c92d9df4e37388bcf2 840w, https://mintcdn.com/pinecone/YhGPIXwx2i0D3QjI/images/integrations/ai-engine.png?w=1100&fit=max&auto=format&n=YhGPIXwx2i0D3QjI&q=85&s=e53c131d82b5f449260ab2343828fe91 1100w, https://mintcdn.com/pinecone/YhGPIXwx2i0D3QjI/images/integrations/ai-engine.png?w=1650&fit=max&auto=format&n=YhGPIXwx2i0D3QjI&q=85&s=5f1e8036fe3786c759f393c61314ef8a 1650w, https://mintcdn.com/pinecone/YhGPIXwx2i0D3QjI/images/integrations/ai-engine.png?w=2500&fit=max&auto=format&n=YhGPIXwx2i0D3QjI&q=85&s=19614a37f844a259b682db1b33b5f8af 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">AI Engine</h2>
    <p>Create intelligent chatbots, generate content, build AI forms, and automate tasks — all from your WordPress dashboard.</p>
  </Card>

  <Card href="/integrations/airbyte">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/airbyte.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=82f0511cc3ac3bc9c24c191eca370667" data-og-width="34" width="34" data-og-height="35" height="35" data-path="images/integrations/airbyte.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/airbyte.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d21f784ba90ef1f633c7fd4f3020b646 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/airbyte.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a22cda098f352089a0d9783ebbd11383 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/airbyte.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=70faa7da3195a33a554406d7f76e8fa2 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/airbyte.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=351fa7b4da236457321e73124d6c2c2b 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/airbyte.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a181f0f5bef5c8860feea7cf55d8722f 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/airbyte.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a26f6f4297176ff31bbf3153bfc1baef 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Airbyte</h2>
    <p>Seamlessly integrate, transform, and load data into Pinecone from hundreds of systems, including databases, data warehouses, and SaasS products.</p>
  </Card>

  <Card href="/integrations/amazon-bedrock">
    <div className="integration-logo">
      <BedrockIcon />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">Amazon Bedrock</h2>
    <p>Integrate your enterprise data into Amazon Bedrock using Pinecone to build highly performant GenAI applications.</p>
  </Card>

  <Card href="/integrations/amazon-sagemaker">
    <div className="integration-logo">
      <SagemakerIcon />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">Amazon Sagemaker</h2>
    <p>Integrate machine learning models seamlessly with a fully-managed service that enables easy deployment and scalability.</p>
  </Card>

  <Card href="/integrations/anyscale">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/anyscale.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=9711e3a780902d158e98a7e2357b255d" data-og-width="34" width="34" data-og-height="34" height="34" data-path="images/integrations/anyscale.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/anyscale.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=30cb2eb2ccb135acb1befb85da49c807 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/anyscale.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=752501972906d9da7920739e0ec94fef 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/anyscale.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=da1615462e87b5630812d741fce0959a 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/anyscale.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=970a990e9f510bea49ab8827b55c8598 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/anyscale.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=511a8af3d17cff54668c747049afdd5c 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/anyscale.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=2cbcdc9ca11329f50ddeb307eb45bb4f 2500w" />
    </div>

    <span className="eyebrow">Models</span>
    <h2 className="font-semibold text-base">Anyscale</h2>
    <p>Focus on building applications powered by LLMs without the need to worry about the underlying infrastructure.</p>
  </Card>

  <Card href="/integrations/apify">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/apify.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=fade046ffd954bfde6c58cbf9bfc7d88" data-og-width="49" width="49" data-og-height="50" height="50" data-path="images/integrations/apify.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/apify.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=98cd11ad236190f4be9b755203edc0e4 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/apify.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7a0b9fa0cf950c73d34dc02f3b3196b2 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/apify.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=568b908db6e102fb489fbd9c56921a40 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/apify.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e0323e6eb07aaef5c736c832b1d53e60 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/apify.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3154210be3b7c9171d2aeb7f54c6ce65 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/apify.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=97ae725d1b71e8eb6fe77dd9bc0db361 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Apify</h2>
    <p>Integrate results from web scrapers or crawlers into a vector database to support RAG or semantic search over web content.</p>
  </Card>

  <Card href="/integrations/aryn">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aryn.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=975621c4bb7044420faf5c7382c3bc59" data-og-width="434" width="434" data-og-height="434" height="434" data-path="images/integrations/aryn.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aryn.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=5be00de1ffd8a43967f67d16f30eccc2 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aryn.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=ef3fbb24681ccbf9344680621c0a1d20 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aryn.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3d20522b9a92ade7e3cc6af5f14766b8 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aryn.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=f393440390d28fb5afb26084e1e8dfbe 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aryn.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=91d6a217c38c07efb3b2da8de80e4871 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aryn.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d6d48b596b53d2a1c6d646758ccd3d7f 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Aryn</h2>
    <p>Process complex, unstructured documents with a purpose-built ETL system for RAG and GenAI applications.</p>
  </Card>

  <Card href="/integrations/aws-marketplace">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aws.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=450374ce6c2900bc89bb92b94ea6e5e3" data-og-width="50" width="50" data-og-height="30" height="30" data-path="images/integrations/aws.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aws.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=4983a0afd5829bd677fb8d1308017650 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aws.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=4cd1a634ce597afeaed90095a60f8d89 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aws.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=8a1b605f1fa8694e61bd0b3ca918b0b9 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aws.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=58999ab37e55d0404ad4467d0f67c15c 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aws.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=c588b971b8f2eee166d1ac3f07180bed 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/aws.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=cc98c366d72c89692a95c140f9429447 2500w" />
    </div>

    <span className="eyebrow">Infrastructure</span>
    <h2 className="font-semibold text-base">AWS Marketplace</h2>
    <p>Access Pinecone through our AWS Marketplace listing.</p>
  </Card>

  <Card href="/integrations/box">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/box.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=732014323042c3228d027c75def2911a" data-og-width="50" width="50" data-og-height="50" height="50" data-path="images/integrations/box.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/box.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e9787f8a415c195c6d101c5d24f968b4 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/box.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=0797ade9b8094958bc047463d4eddd34 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/box.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=2c3c415f6378cfc0113b177f3d7c475c 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/box.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=77fdc47455f63e794e5a4a1b496157c4 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/box.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=90ac0a67642606578cf4cb45a8de03a2 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/box.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=31b536151b1f779fa41ec9b13cbc07b0 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Box</h2>
    <p>Connect a Box account to a Pinecone vector database.</p>
  </Card>

  <Card href="/integrations/cloudera">
    <div className="integration-logo-long">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cloudera.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=f0096b3df1cb4c19af1afeedf355874c" data-og-width="4000" width="4000" data-og-height="488" height="488" data-path="images/integrations/cloudera.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cloudera.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=c3fbfb651f35f5ce82d3baa8ca1f911a 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cloudera.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b399c0c2b563187f55a5c8541adb7e22 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cloudera.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=c287752bfd014fbb99815aa23765a42f 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cloudera.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b54336cf1a5de8e245ee4b92a74c18c8 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cloudera.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=ce77be306a6f920e3407cb51b9001d69 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cloudera.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=875c300f0a32724fde4566a1b5869c8c 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">Cloudera AI</h2>
    <p>Vector embedding, RAG, and semantic search at scale.</p>
  </Card>

  <Card href="/integrations/cohere">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cohere.svg?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=f022fd70f49bfac8d8fbe1ef8e57065f" data-og-width="34" width="34" data-og-height="34" height="34" data-path="images/integrations/cohere.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cohere.svg?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=697689a8c52d0aa0b23e3e636378c185 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cohere.svg?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=272cbfa8156f2ba69455b97d1ebdfb28 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cohere.svg?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=41ee75721da3d3757ea6f2eef7cc2ecd 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cohere.svg?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=68b44026bab90699a1fa84c5eaad15d8 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cohere.svg?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=9dc3d1372c5fb9455dd7b8d973802b6b 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/cohere.svg?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=c13101efba6aea8ec75b0c67a93920a6 2500w" />
    </div>

    <span className="eyebrow">Models</span>
    <h2 className="font-semibold text-base">Cohere</h2>
    <p>Leverage cutting-edge natural language processing tools for enhanced text understanding and generation in your applications.</p>
  </Card>

  <Card href="/integrations/confluent">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/confluent.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=cb141bceada6b4aff7889f5b59c5deed" className="dark-inverted" data-og-width="34" width="34" data-og-height="34" height="34" data-path="images/integrations/confluent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/confluent.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=87857a99c97f6b698702bf0555571af4 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/confluent.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b0b7ae7f68204905417efe3223ecee94 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/confluent.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e5ea308d9b2741f995cbaeb8bd0fcf0f 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/confluent.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=8aa9ff01e3cc0476eae3c804c853ce27 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/confluent.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=5c4481af63372f9065404d3b2fd5cd27 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/confluent.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=95cec14e1c5a2c56117f55076ac7de44 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Confluent</h2>
    <p>Connect and process all of your data in real time with a cloud-native and complete data streaming platform.</p>
  </Card>

  <Card href="/integrations/context-data">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/context-data.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=af300f1a6fa4ddc347d7fe6f56015e99" data-og-width="500" width="500" data-og-height="500" height="500" data-path="images/integrations/context-data.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/context-data.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=6842373c49c73806378fc833dbce3df7 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/context-data.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3e61e2aafed01d890575bf9fb8bb951f 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/context-data.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=77a1440a7bda844cf262c2b0376ff78d 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/context-data.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=680dedfe00f70d39b12dea3dbf85b647 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/context-data.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=83a816ca8a9936ccde9a0105dc5e5fea 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/context-data.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=6719d5caff983f6f241bfaa7d0986a8e 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">Context Data</h2>
    <p>Create end-to-end data flows that connect data sources to Pinecone.</p>
  </Card>

  <Card href="/integrations/databricks">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/databricks.svg?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=0e5d77b880ab284937681f209f2e20d2" data-og-width="50" width="50" data-og-height="50" height="50" data-path="images/integrations/databricks.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/databricks.svg?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e982cd5cd65b90f331e265b3ed03f971 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/databricks.svg?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7d8a658653604c4e1f50758dfd32c9f7 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/databricks.svg?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d306798bb54828c39c5bcd999c3fb7b4 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/databricks.svg?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=9eda9627f313e89a7d42a202a7aaa894 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/databricks.svg?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=06cd06f7f51569bafa737af33149dd50 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/databricks.svg?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3d49d7caeef1750b1b47ddbfc6c76cec 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Databricks</h2>
    <p>Combine the power of a unified analytics platform with Pinecone for scalable data processing and AI insights.</p>
  </Card>

  <Card href="/integrations/datadog">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datadog.svg?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=740f28ee7b7e1d6f3370431586768a04" data-og-width="50" width="50" data-og-height="50" height="50" data-path="images/integrations/datadog.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datadog.svg?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=90285c88aec0452bb85ecd6d376e5431 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datadog.svg?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=410ca8cfab3be7a612b238f144f23668 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datadog.svg?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=75aa2558a9551e57b60ad35fe41b7606 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datadog.svg?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b48fd79a76c2c4b9fc698530d3e36734 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datadog.svg?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e4c5c396edb1e2113db7619dff253e5f 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datadog.svg?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7533b6c38c6f6f307f274e496acb9ecb 2500w" />
    </div>

    <span className="eyebrow">Observability</span>
    <h2 className="font-semibold text-base">Datadog</h2>
    <p>Monitor and secure your applications by integrating with a cloud-scale monitoring service that provides real-time analytics.</p>
  </Card>

  <Card href="/integrations/datavolo">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datavolo.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=aefdd0412541ab3fb2e50bbd32894b41" data-og-width="2360" width="2360" data-og-height="1261" height="1261" data-path="images/integrations/datavolo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datavolo.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=35f42f7431712f3146207780e0d6a2b4 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datavolo.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=fa8d2500aada1a60e407a9948b0215f6 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datavolo.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=854e3ab626686e5453bd828ee58a8eba 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datavolo.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d0452512a3fbcd14987634d01aeffe72 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datavolo.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=46fbb1d66154a2b34ed1f4f1b6d0dff5 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/datavolo.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=dc636ff5d8efb517fcd134576c281394 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Datavolo</h2>
    <p>Source, transform, and enrich data in a continuous, composable and customizable manner.</p>
  </Card>

  <Card href="/integrations/estuary">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/estuary.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=6b8e1be3fbaac36951046f83506ec608" data-og-width="50" width="50" data-og-height="50" height="50" data-path="images/integrations/estuary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/estuary.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=8620fff0c6220238721421686a210711 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/estuary.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=cbd080792e409f31f9cc6893f7da7e40 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/estuary.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=251614604fc74ace10e5655836fe7c9b 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/estuary.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=07ff3e102abf9ce7cdfcee5ad0c838e5 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/estuary.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b31d73fb8c5d8fc89cb9d212f44ac455 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/estuary.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=930dfa16519771797748494a9b626c36 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Estuary</h2>
    <p>Source data from hundreds systems and push data to Pinecone, for an always up-to-date view.</p>
  </Card>

  <Card href="/integrations/flowise">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/flowise.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d3cfc5e92201ebf64cd6f4ce383062ba" data-og-width="300" width="300" data-og-height="300" height="300" data-path="images/integrations/flowise.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/flowise.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=ede4f62d43d9c7c17af6bedb9467ea4f 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/flowise.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=5d6a6a98ed040814bc0e8e9dcdb3bb32 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/flowise.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a26bfa59c91798fb87f5d46feb951f50 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/flowise.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b3091bb78dc5b29e9ab3ed849387ad00 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/flowise.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=81bae48c0ac0ba572db434d2d64eafdc 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/flowise.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=6fe5c41333d21f9371986a6e57298973 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">FlowiseAI</h2>
    <p>Build customized LLM apps with an open source, low-code tool for developing orchestration flow & AI agents.</p>
  </Card>

  <Card href="/integrations/fleak">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/fleak.svg?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7d4010b2293cedff791a5578e6e1e324" data-og-width="185" width="185" data-og-height="197" height="197" data-path="images/integrations/fleak.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/fleak.svg?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=c9eb0fdf2fb7004a8f32033b0ada5e40 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/fleak.svg?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e97588cbc7b21ed69961a862d7b47eca 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/fleak.svg?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=40d01374af1054609a897226eee41826 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/fleak.svg?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=81eff268aaca37e843f476c122deb99d 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/fleak.svg?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d078165802510068956f68d90fe8389b 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/fleak.svg?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=854d7da5e9a00d104ad7915b46047f9a 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Fleak</h2>
    <p>Build, deploy, and manage complex workflows with a low-code platform for AI-assisted ML and LLM transformations.</p>
  </Card>

  <Card href="/integrations/gathr">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/gathr.svg?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=622ed186facb86bf53407e3997f93a81" data-path="images/integrations/gathr.svg" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Gathr</h2>
    <p>Build and operationalize data and AI-driven solutions at scale.</p>
  </Card>

  <Card href="/integrations/google-cloud-marketplace">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/gcp.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=6d86fdcad91fb4266758cc85ae899b81" data-og-width="40" width="40" data-og-height="32" height="32" data-path="images/integrations/gcp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/gcp.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=6b60bbebbc43ac164f43b135dd950bad 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/gcp.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b8c36ac69608b6f57cc8d1682ce79988 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/gcp.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=93634ce4880cd52d7ab0708375820a32 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/gcp.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=4ffe868dbb19fa691ca2fd3b6ac0e18c 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/gcp.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=8d684fe49459760700993fcf999f4db2 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/gcp.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d09a82720507a1e7c40ca90d4e336d2e 2500w" />
    </div>

    <span className="eyebrow">Infrastructure</span>
    <h2 className="font-semibold text-base">Google Cloud Marketplace</h2>
    <p>Access Pinecone through our Google Cloud Marketplace listing.</p>
  </Card>

  <Card href="/integrations/genkit">
    <div className="integration-logo-long">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/genkit.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=eac4e66270a48feb93e1f4c2e4596764" data-og-width="818" width="818" data-og-height="167" height="167" data-path="images/integrations/genkit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/genkit.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=0a54320d137e3ec3f86f9332bfb0818b 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/genkit.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=9c2c87a3f437f294da3644b3aaf4c065 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/genkit.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d01cdf0450ce4d5d80ffb874ed2fad87 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/genkit.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=76a593493ef8534c3d7b8609d2c19142 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/genkit.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=f0729c4e5c4f5ca339513480765fe215 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/genkit.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=ef482aaa10fdf972b375e7bbef86f9ee 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">Genkit</h2>
    <p>Build AI powered applications and agents.</p>
  </Card>

  <Card href="/integrations/github-copilot">
    <div className="integration-logo">
      <img className="dark-inverted" src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/github-copilot.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=55bb18085ef97dff0efdeb2f5afad058" data-og-width="240" width="240" data-og-height="240" height="240" data-path="images/integrations/github-copilot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/github-copilot.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e2e19a5467ed6825e918e0ec80dedc51 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/github-copilot.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=0a95b9756415ebbe78d933a787350ce7 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/github-copilot.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=24a24f86adfbcd141c734d85b0d6823f 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/github-copilot.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=624c6e631790a8478808ded2bfc85344 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/github-copilot.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=2f2d1fb27960781db630acca84749999 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/github-copilot.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3133e629f9da1c1ce101aff133e16de4 2500w" />
    </div>

    <span className="eyebrow">Infrastructure</span>
    <h2 className="font-semibold text-base">GitHub Copilot</h2>
    <p>Get personalized recommendations that enable you to retrieve relevant data and collaborate effectively with Copilot.</p>
  </Card>

  <Card href="/integrations/haystack">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/haystack.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=56e03431f80e0f1bb2b70fea1a3258c7" data-og-width="34" width="34" data-og-height="34" height="34" data-path="images/integrations/haystack.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/haystack.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=9e0c7c5d2373dc2c4a0d2fa9a743397b 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/haystack.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=54474cadfdc2d6737e18a9fd9c906838 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/haystack.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a2e2c7900c4daba2bab2a7d017c45bbe 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/haystack.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3c3e7dc6796de2b46c0dc47558fe111b 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/haystack.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e229637c7f75992dc7debb0a4a8bd965 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/haystack.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e5f4152248ee633a945f8969144963b6 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">Haystack</h2>
    <p>Implement an end-to-end search pipeline for efficient retrieval and question answering over large datasets.</p>
  </Card>

  <Card href="/integrations/honeyhive">
    <div className="integration-logo-long">
      <img className="dark-inverted" src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/honeyhive.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=f98500a3e97abca67649d778ad1112b0" data-og-width="5064" width="5064" data-og-height="1034" height="1034" data-path="images/integrations/honeyhive.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/honeyhive.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=83feb2d47d332bf8d4e351e2d7564b73 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/honeyhive.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=6152e48b701f6f5d0351f5c44fb6b864 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/honeyhive.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=f610bca496e19e432e8ae0e9ef1ab75d 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/honeyhive.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=ebe8379629a7a065efeaa96fe2fbd96f 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/honeyhive.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b5bed79f933f2511e8b5012da2d4d2d3 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/honeyhive.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=922d1243ccdc8892fc99ecb8ac66de10 2500w" />
    </div>

    <span className="eyebrow">Observability</span>
    <h2 className="font-semibold text-base">HoneyHive</h2>
    <p>Clearly visualize your execution traces and spans.</p>
  </Card>

  <Card href="/integrations/hugging-face-inference-endpoints">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/huggingface.svg?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=be3d5a18a21c9210871079bcfc7f346c" data-og-width="42" width="42" data-og-height="38" height="38" data-path="images/integrations/huggingface.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/huggingface.svg?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=044aab8178145993b9c34588336ba0f5 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/huggingface.svg?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=301a1c883bd2d637fe7e94341f7e99ca 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/huggingface.svg?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d47ec438d11f78adcaba2a5aba63c42f 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/huggingface.svg?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=f0f70c4090b80477e265b45262a72e2a 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/huggingface.svg?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a21f40582d24633b321398500d73c072 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/huggingface.svg?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=ec0cd7b0e6b18eee9eb3ebc77f06f5ce 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">Hugging Face</h2>
    <p>Deploy state-of-the-art machine learning models on scalable infrastructure, streamlining the path from prototype to production.</p>
  </Card>

  <Card href="/integrations/instill">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/instill.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=777fcd742c95c16aa04410940cdf61ea" data-og-width="50" width="50" data-og-height="50" height="50" data-path="images/integrations/instill.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/instill.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=2df524d575114486e138325d4ec37d6b 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/instill.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=c512423a3f9d9f6a16fd8836f15dfa37 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/instill.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=17f0573047ffbbf8c9e26289fa6f4c96 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/instill.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=c2f31fc7bdc6578296131861bd693aff 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/instill.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=bf6bc20a42ffb214a7fe8f20b914e68d 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/instill.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=444549d8a59e90be570aa35658fd24d7 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">Instill AI</h2>
    <p>Streamline AI development with a low-code full-stack infrastructure tool for data, model, and pipeline orchestration.</p>
  </Card>

  <Card href="/integrations/jina">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/jina.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b3fb233a5438f771e10cc94061a49188" data-og-width="50" width="50" data-og-height="21" height="21" data-path="images/integrations/jina.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/jina.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a2936d6539529daaffc9ca606a68afa1 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/jina.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=98c7a4ba4d290132308fa75504d9377b 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/jina.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=42d967e42123987b6390f03c68ba0655 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/jina.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e6cbe6aa6f36fe7cead941e89260859d 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/jina.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e1d1437a26f446f0e01be493c2ad1619 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/jina.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=45878b33c57a5382570502a28b1c76bf 2500w" />
    </div>

    <span className="eyebrow">Models</span>
    <h2 className="font-semibold text-base">Jina</h2>
    <p>Leverage powerful AI models to generate high-quality text embeddings, fine-tuned to both domain- and language-specific use cases.</p>
  </Card>

  <Card href="/integrations/langchain">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langchain.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=0bf433738cc115904657a4eecac7964d" data-og-width="34" width="34" data-og-height="18" height="18" data-path="images/integrations/langchain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langchain.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b194412589073ca61aa79b292319d90b 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langchain.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e194ff5c930651766d63cf62ec31b8e9 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langchain.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b5bb7f5f382e02746012371ecbaf1519 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langchain.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=6a980be11e4ce7283609074bc9277709 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langchain.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d44213125c8489fa94838556868f118b 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langchain.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=1685e08efd2ad34e54dd679c62ab7c44 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">LangChain</h2>
    <p>Combine language models with chain-of-thought reasoning for advanced problem solving and decision support.</p>
  </Card>

  <Card href="/integrations/langtrace">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langtrace.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e0096cc1c765813803df3579e502f763" data-og-width="512" width="512" data-og-height="512" height="512" data-path="images/integrations/langtrace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langtrace.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=01aa0745442d3e8987deec9cc2949611 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langtrace.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=2a3fcf740f03a29a6ec0fad28fc53ec3 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langtrace.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=3c54c9234ad89d3de3016ca602ae3d12 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langtrace.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=fbd33b3aeb64c305b724c2d08c12be14 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langtrace.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=51889f35a213bd3cef50fb50ecc29dad 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/langtrace.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=18057d68d5ee0c98054b1008f09ac904 2500w" />
    </div>

    <span className="eyebrow">Observability</span>
    <h2 className="font-semibold text-base">Langtrace</h2>
    <p>Access rich and high cardinal tracing for Pinecone API calls, ingestible into your observability tool of choice.</p>
  </Card>

  <Card href="/integrations/llamaindex">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/llamaindex.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=1bda5b90e9ad147cc4a90b624ec95058" data-og-width="26" width="26" data-og-height="34" height="34" data-path="images/integrations/llamaindex.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/llamaindex.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d05c39c28a654549be68d3b3cc35d296 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/llamaindex.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=81c870b9ae0067b8d1fde8c61bb3bc80 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/llamaindex.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a7afa59c4d4dee888e1e6c17d2b48451 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/llamaindex.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=8e489ab8ad9b7050e83f152ec3dc4e93 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/llamaindex.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=fd2b72a887677662e3a45fddd2e2cc98 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/llamaindex.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e34a36fabc898ba5317ccaa4278385bf 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">Llama Index</h2>
    <p>Leverage Llama for indexing and retrieving information at scale, improving data access and analysis.</p>
  </Card>

  <Card href="/integrations/matillion">
    <div className="integration-logo-long">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/matillion.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=1dca8685dd07ab23626c88b0f26799ec" data-og-width="1200" width="1200" data-og-height="1201" height="1201" data-path="images/integrations/matillion.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/matillion.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b479197488207d5a787765e1ed83b7ed 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/matillion.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=47f9b6202270fa0d24c4d4a271d2a485 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/matillion.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e89f72b5bfdf1d6fcff25b58f56e975c 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/matillion.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=ba90cc0608099fba473659b8c3b8aafc 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/matillion.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=97a59c70998a32a3b8d60b0cd89d2227 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/matillion.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=f11b0212f9392560e3631599eb6fae8d 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Matillion</h2>
    <p>Easily create and maintain data pipelines, build custom connectors for any source, and enjoy AI and high-code options to suit any need.</p>
  </Card>

  <Card href="/integrations/microsoft-marketplace">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/azure.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=bbcb055c142f796e3bd1769efa5112df" data-og-width="34" width="34" data-og-height="32" height="32" data-path="images/integrations/azure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/azure.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d9d4310c4202138f8ee1c6f6d68e73ed 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/azure.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=332e8477ee6ae42d383dcf7c85a443e9 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/azure.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=91ded9121b1d9a37b9681f4627057926 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/azure.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e1d36ffede7bfe396579353de5aa6230 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/azure.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=6b58640a60f3fe3d13b9420ce2817b86 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/azure.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b04ea40a4e8c9ab291545dbff654ed45 2500w" />
    </div>

    <span className="eyebrow">Infrastructure</span>
    <h2 className="font-semibold text-base">Microsoft Marketplace</h2>
    <p>Access Pinecone through our Microsoft Marketplace listing.</p>
  </Card>

  <Card href="/integrations/new-relic">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/new-relic.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=ff34e204c22601c7ec5d258116b89dca" data-og-width="29" width="29" data-og-height="34" height="34" data-path="images/integrations/new-relic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/new-relic.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=043c8a0f66129a9d4bdbad5106f4449f 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/new-relic.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=ea687dd2a59e83fc7c487ce866ac343e 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/new-relic.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=894e61fc148a345cfd441a10a81ccf5f 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/new-relic.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=70ec2f611acc35e848fb398f18a0d530 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/new-relic.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=8737e80920ae4be25358149dfd65bad3 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/new-relic.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=463cf087b12fe5ebe6fe912e7f05b1e8 2500w" />
    </div>

    <span className="eyebrow">Observability</span>
    <h2 className="font-semibold text-base">New Relic</h2>
    <p>Implement monitoring and integrate your Pinecone application with New Relic for performance analysis and insights.</p>
  </Card>

  <Card href="/integrations/nexla">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nexla.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=64b0f621cda6fa3c0d739c281859ef97" data-og-width="400" width="400" data-og-height="400" height="400" data-path="images/integrations/nexla.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nexla.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=4b2fb6a86ed66055570c80bed624853b 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nexla.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=8a4fe8b96f213d919ae94f6a36696dfa 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nexla.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=1141e94b84d179e091fb5b9ce0683b5e 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nexla.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=5ce302c92b3f1be06dbed915ded5514d 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nexla.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=c0f783d70a240547f7122d2a42c30ae3 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nexla.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=c4f5144e6a9472dc3d26f5b024f69a1c 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Nexla</h2>
    <p>Ingest data from 500+ connectors with Nexla's low-code/no-code AI integration platform.</p>
  </Card>

  <Card href="/integrations/nuclia">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nuclia.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=01ec2f4ebfe0d9cf4be0940a9312c8c7" data-og-width="50" width="50" data-og-height="50" height="50" data-path="images/integrations/nuclia.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nuclia.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=fe867b3d6a828c2ddee213c96d44380a 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nuclia.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a10f2c9396cd4ae06a9c7a009de8d4de 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nuclia.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=162f11f3b2e53a4013fa09e6eddc54de 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nuclia.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=051a641bdae5d9a183a198cde4f074fc 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nuclia.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=1bddd4f184ccc5843492fd1ea009c912 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/nuclia.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=04a75c1c05ff389b11f77d62a80c7183 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">Nuclia</h2>
    <p>Nuclia RAG-as-a-Service automatically indexes files and documents from both internal and external sources.</p>
  </Card>

  <Card href="/integrations/octoai">
    <div className="integration-logo-long">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/octoai.svg?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=c75a8b985a02a1c1a9361928881422d7" data-og-width="1104" width="1104" data-og-height="336" height="336" data-path="images/integrations/octoai.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/octoai.svg?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b271d623c04b4e10af76423065973968 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/octoai.svg?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=55e53e52cc4f07e5f72b2578c071dabf 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/octoai.svg?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d3d576e35315b6c8af5ad8bc68a0e9ac 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/octoai.svg?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=a03804d664c4778b126820efc88e026f 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/octoai.svg?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b7394468480d4d51f650f40205667010 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/octoai.svg?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=9fa76562daad0db31a57a604255e10de 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">OctoAI</h2>
    <p>Harness value from the latest AI innovations by delievering efficient, reliable, and customizable AI systems for your apps.</p>
  </Card>

  <Card href="/integrations/openai">
    <div className="integration-logo">
      <OpenAIIcon />
    </div>

    <span className="eyebrow">Models</span>
    <h2 className="font-semibold text-base">OpenAI</h2>
    <p>Access powerful AI models like GPT for innovative applications and services, enhancing user experiences with AI capabilities.</p>
  </Card>

  <Card href="/integrations/pulumi">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/pulumi.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=5a02b6d8249d87a490ecdc2f4f0ba166" data-og-width="34" width="34" data-og-height="34" height="34" data-path="images/integrations/pulumi.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/pulumi.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=643904d292f65504eac995079f4f36ec 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/pulumi.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=4c35451b3840d5ba3bfdec12091d5222 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/pulumi.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=85f04ede2f4054af0f4ecf8a51dd3343 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/pulumi.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=05971285cc9eb49d012f2037d36e50e3 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/pulumi.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7dcea39521ff52d9ca3519f8c1fd3ad1 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/pulumi.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=4de6d115edd5323cebc82360edc99fb4 2500w" />
    </div>

    <span className="eyebrow">Infrastructure</span>
    <h2 className="font-semibold text-base">Pulumi</h2>
    <p>Manage your Pinecone collections and indexes using any language of Pulumi Infrastructure as Code.</p>
  </Card>

  <Card href="/integrations/redpanda">
    <div className="integration-logo-long">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/redpanda.svg?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=38c41060e25e38652bff7940d56567ae" data-og-width="155" width="155" data-og-height="36" height="36" data-path="images/integrations/redpanda.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/redpanda.svg?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=ba3979ea5e7a3a33e2f3da3e0758c40d 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/redpanda.svg?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=dccbe732367c8b79a40ab98e1bbd007e 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/redpanda.svg?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e5c82d05b5726f348f8620090444a94d 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/redpanda.svg?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=cbd23ed907e5ff25e98686ce544307fe 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/redpanda.svg?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=9a0bafefb545875a6697a74e2bcceec8 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/redpanda.svg?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=d734c80264594ad1f1dbb018e5f5f242 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Redpanda</h2>
    <p>Connect existing data sources to Pinecone with a Kafka-compatible streaming data platform built for data-intensive applications.</p>
  </Card>

  <Card href="/integrations/snowflake">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/snowflake.png?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=70e845761641a778eec1747ad0d4f921" data-og-width="34" width="34" data-og-height="34" height="34" data-path="images/integrations/snowflake.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/snowflake.png?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=c98762a6b88b31589bfdafdac53fb5ec 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/snowflake.png?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=0741b285a3a3ff9dcf2303e0fe4de6c2 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/snowflake.png?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=90b6b4696695d2492433b1dec65751cc 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/snowflake.png?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=b8bbfe6890780ed81d721ee38970a32a 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/snowflake.png?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=f9a999da1a34d6383e2f57b5a2918272 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/snowflake.png?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=bed28833aebfeb6445d7a7a1327e35a7 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">Snowflake</h2>
    <p>Run Pinecone with Snowpark Container Services, designed to deploy, manage, and scale containerized applications within the Snowflake ecosystem.</p>
  </Card>

  <Card href="/integrations/streamnative">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/streamnative.svg?fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=78e6416d0d142ecc6180b35bebc099e5" style={{ width: '50px', height: '50px', objectFit: 'contain' }} data-og-width="96" width="96" data-og-height="152" height="152" data-path="images/integrations/streamnative.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/streamnative.svg?w=280&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7a438a5701a17de25ed219d6679b6022 280w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/streamnative.svg?w=560&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=73b46a4af9ace39b62cc1d859c8a7418 560w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/streamnative.svg?w=840&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=ae1552b895005837225cb25d7afefe70 840w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/streamnative.svg?w=1100&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=e65e8cbaf602d4bdeff52fd5ed966f44 1100w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/streamnative.svg?w=1650&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=7dafed162523479af1ed5ddbfe3fb4c9 1650w, https://mintcdn.com/pinecone/-4J8tNwjqgTl1iBy/images/integrations/streamnative.svg?w=2500&fit=max&auto=format&n=-4J8tNwjqgTl1iBy&q=85&s=530ceb9f3dc0b8d0f3847566753bb2d7 2500w" />
    </div>

    <span className="eyebrow">Data Sources</span>
    <h2 className="font-semibold text-base">StreamNative</h2>
    <p>A scalable, resilient, and secure messaging and event streaming platform.</p>
  </Card>

  <Card href="/integrations/terraform">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/terraform.svg?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=3069af3058021a3f5640e67beaa70a40" data-og-width="800" width="800" data-og-height="800" height="800" data-path="images/integrations/terraform.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/terraform.svg?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=7252c1883b8cb7db9a96c9f2dd569a7a 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/terraform.svg?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=efcbeba2099e07fa4459835e03abbdbb 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/terraform.svg?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=5b2f00062fd53f7a6ea35ff7197e7c01 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/terraform.svg?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=d61a3fbe95a209948e0df17dcbf91e0d 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/terraform.svg?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=4da3aeba83c0ec9e59abcc4ceb6a77e0 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/terraform.svg?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=dfd5792450dbc563df065cb058be9974 2500w" />
    </div>

    <span className="eyebrow">Infrastructure</span>
    <h2 className="font-semibold text-base">Terraform</h2>
    <p>Manage your infrastructure using configuration files for a consistent workflow.</p>
  </Card>

  <Card href="/integrations/traceloop">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/traceloop.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=3d27ca8106c56a2408b84d8d9ddf2e9d" style={{ width: '50px', height: '50px', objectFit: 'contain' }} data-og-width="702" width="702" data-og-height="878" height="878" data-path="images/integrations/traceloop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/traceloop.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=f43d9f00111ae0f95d004a41ff64872e 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/traceloop.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=0a01a49956f843926f39d6913d0c5aa2 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/traceloop.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=c73c7052ddbe0e78c6dac1b5570ebb8a 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/traceloop.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=a4c7d1792ddacdf52cfbf4c06784b571 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/traceloop.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=17494b45bfa08e76483a0843947c4f75 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/traceloop.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=ca390ba0c162382eedb45f57ae50cc18 2500w" />
    </div>

    <span className="eyebrow">Observability</span>
    <h2 className="font-semibold text-base">Traceloop</h2>
    <p>Produce traces and metrics that can be viewed in any OpenTelemetry-based platform.</p>
  </Card>

  <Card href="/integrations/trulens">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/trulens.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=bc486fd4b07de8df11fd316a713077ef" data-og-width="34" width="34" data-og-height="34" height="34" data-path="images/integrations/trulens.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/trulens.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=260f28f09f73a346962f798a3e12adec 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/trulens.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=ab7d473e5d5ddbe60ca7fa4bb632de1c 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/trulens.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=e3b609d4dc19275654130d92be1b36ba 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/trulens.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=7adb2d4f2ef29d462232a23dfaf3a9af 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/trulens.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=9a0a4e0a69791d116d09bb46b38c7f48 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/trulens.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=0f9071f127ee18ff66b3c4c1b9b12f07 2500w" />
    </div>

    <span className="eyebrow">Observability</span>
    <h2 className="font-semibold text-base">TruLens</h2>
    <p>Gain insights into your machine learning models' decisions, improving interpretability and trustworthiness.</p>
  </Card>

  <Card href="/integrations/twelve-labs">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/twelve-labs.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=cbfeeb44f58ddc2fb4c4aa9e0dacbe84" data-og-width="1200" width="1200" data-og-height="1200" height="1200" data-path="images/integrations/twelve-labs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/twelve-labs.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=14f75b1988def87ce050f19af0ff173c 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/twelve-labs.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=d4d58d3a11577f8768cefac9e3662c87 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/twelve-labs.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=19ef99a49a8e569030b9fc749379df5c 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/twelve-labs.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=e08906c81f5cec2160af6676befd1886 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/twelve-labs.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=8084cd2d9f7d1ee8f8b6f26e52c38e11 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/twelve-labs.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=f8e1afc1a1f58219f340576254175e69 2500w" />
    </div>

    <span className="eyebrow">Models</span>
    <h2 className="font-semibold text-base">Twelve Labs</h2>
    <p>Create high-quality multimodal embeddings that capture the rich context and interactions between different modalities in videos.</p>
  </Card>

  <Card href="/integrations/unstructured">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/unstructured.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=2ed3cf2fb6277f97ff6811683d98bf6c" data-og-width="50" width="50" data-og-height="50" height="50" data-path="images/integrations/unstructured.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/unstructured.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=9371d00e76b0a4ae05827a7886095003 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/unstructured.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=63f90d11c282a1c4c319c1dc6af835a2 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/unstructured.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=55e5d1b429bd9d9b5312902aa31ba0c5 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/unstructured.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=82a6482d74d93f7c203037f224d333cc 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/unstructured.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=daaf5e57aa7090143c978eda17790060 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/unstructured.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=c4def2b79d053cbd0e0e4c3543f91fd4 2500w" />
    </div>

    <span className="eyebrow">Data Source</span>
    <h2 className="font-semibold text-base">Unstructured</h2>
    <p>Load data into Pinecone with a single click.</p>
  </Card>

  <Card href="/integrations/vercel">
    <div className="integration-logo">
      <img src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/vercel.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=b35d6a3bdf590f2f735c40eb6deea684" className="dark-inverted" data-og-width="39" width="39" data-og-height="34" height="34" data-path="images/integrations/vercel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/vercel.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=509445c35744fe1ca3ae66a366810105 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/vercel.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=ee363ec056b9a3bfa1d300f76b11cd54 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/vercel.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=78956a758bfe82d39e849e482349f34c 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/vercel.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=761cb725d29f6dd58d66f0d06400dc1f 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/vercel.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=606341b0700417288735b3a818cebd97 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/vercel.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=58f086f4bac5ae4e04cec4f4aca65264 2500w" />
    </div>

    <span className="eyebrow">Infrastructure</span>
    <h2 className="font-semibold text-base">Vercel</h2>
    <p>Use Pinecone as the long-term memory for your Vercel AI projects, and easily scale to support billions of data points.</p>
  </Card>

  <Card href="/integrations/voltagent">
    <div className="integration-logo">
      <img className="dark-inverted" src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voltagent.svg?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=caeb2a720d8561984db1ec8e5192d7d4" data-og-width="649" width="649" data-og-height="162" height="162" data-path="images/integrations/voltagent.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voltagent.svg?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=3d086c4526c0da22fe79c53be13b2ff3 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voltagent.svg?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=faf8736743126cdb383a9b8f82b24b02 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voltagent.svg?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=c99caab2dba563ace51048bdefc64450 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voltagent.svg?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=fa725a9d856370f4217a0ffb59b6b53c 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voltagent.svg?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=5997e0cdd2d6c2aba52a5721963c07a1 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voltagent.svg?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=e66d7d5be097fbebbc1b0c33472234ab 2500w" />
    </div>

    <span className="eyebrow">Frameworks</span>
    <h2 className="font-semibold text-base">VoltAgent</h2>
    <p>A TypeScript-based, AI-agent framework for building AI applications with retrieval-augmented generation (RAG) capabilities.</p>
  </Card>

  <Card href="/integrations/voyage">
    <div className="integration-logo">
      <img className="dark-inverted" src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voyage.svg?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=8ad9ef970510e9420d5df811bb724202" data-og-width="697" width="697" data-og-height="695" height="695" data-path="images/integrations/voyage.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voyage.svg?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=8f0c1f5d920dbc9d11428cf5c674f3c5 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voyage.svg?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=26a2c3b50807f070db719ef053016ff1 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voyage.svg?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=19646b5e560841f797a9b8dfcd0850ce 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voyage.svg?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=b182ecbb50c648cfb1487fcc95a5f6d6 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voyage.svg?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=b4e03e95b29dc3792da87afaec4a7e74 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/integrations/voyage.svg?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=5bee1b83bbd58ccbcc9057ce43c98ae7 2500w" />
    </div>

    <span className="eyebrow">Models</span>
    <h2 className="font-semibold text-base">Voyage AI</h2>
    <p>Cutting-edge embedding models and rerankers for semantic search and RAG.</p>
  </Card>

  <Card href="/integrations/zapier">
    <div className="integration-logo">
      <img className="dark-inverted" src="https://mintcdn.com/pinecone/vm6y8tUlUErsL7WY/images/integrations/zapier.png?fit=max&auto=format&n=vm6y8tUlUErsL7WY&q=85&s=dfe9e863e9cb0890f0101860f77b24ff" data-og-width="500" width="500" data-og-height="136" height="136" data-path="images/integrations/zapier.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/vm6y8tUlUErsL7WY/images/integrations/zapier.png?w=280&fit=max&auto=format&n=vm6y8tUlUErsL7WY&q=85&s=8291b3c5a09092cee91c69d6df801b7b 280w, https://mintcdn.com/pinecone/vm6y8tUlUErsL7WY/images/integrations/zapier.png?w=560&fit=max&auto=format&n=vm6y8tUlUErsL7WY&q=85&s=e8ba322cdddf794dffcd07459398f42e 560w, https://mintcdn.com/pinecone/vm6y8tUlUErsL7WY/images/integrations/zapier.png?w=840&fit=max&auto=format&n=vm6y8tUlUErsL7WY&q=85&s=7cd26b0e330579a67eab382d2fa42cc1 840w, https://mintcdn.com/pinecone/vm6y8tUlUErsL7WY/images/integrations/zapier.png?w=1100&fit=max&auto=format&n=vm6y8tUlUErsL7WY&q=85&s=26b21fad993d0bd2203689b9c36bf9fc 1100w, https://mintcdn.com/pinecone/vm6y8tUlUErsL7WY/images/integrations/zapier.png?w=1650&fit=max&auto=format&n=vm6y8tUlUErsL7WY&q=85&s=23c4fe975b1f4808db771ff2883dd94c 1650w, https://mintcdn.com/pinecone/vm6y8tUlUErsL7WY/images/integrations/zapier.png?w=2500&fit=max&auto=format&n=vm6y8tUlUErsL7WY&q=85&s=a2c22965df2f7d715f6b0876805b211e 2500w" />
    </div>

    <span className="eyebrow">Infrastructure</span>
    <h2 className="font-semibold text-base">Zapier</h2>
    <p>Zapier connects Pinecone to thousands of apps to help you automate your work. No code required.</p>
  </Card>
</CardGroup>



---
**Navigation:** [← Previous](./20-set-environment-variables-for-api-keys.md) | [Index](./index.md) | [Next →](./22-pulumi.md)

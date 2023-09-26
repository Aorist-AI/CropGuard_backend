def html(msg_received):
    amount = msg_received["amount"]
    display_name = msg_received["msg_received"]

    mail_sub = """
     <html>
  <head>
    <title>You've received a gift</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style type="text/css">
      a {
        outline: none;
        color: #fff;
        text-decoration: none;
      }
      a:hover {
        text-decoration: underline !important;
        color: #777a81 !important;
      }
      a[x-apple-data-detectors] {
        color: inherit !important;
        text-decoration: none !important;
      }
      /*			.active:hover{opacity:0.8;}
			*/
      .active {
        -webkit-transition: all 0.3s ease;
        -moz-transition: all 0.3s ease;
        -ms-transition: all 0.3s ease;
        transition: all 0.3s ease;
      }
      .link1 a {
        color: #ff3347 !important;
      }
      .link2 a {
        color: #fff !important;
      }
      .link a:hover {
        text-decoration: none !important;
      }
      a img {
        border: none;
      }
      .no-link span {
        color: inherit !important;
        border: none !important;
      }
      .applelinksblack a {
        color: #fff !important;
        text-decoration: none;
        font: 15px/26px Arial, Helvetica, sans-serif !important;
        color: #fff;
        letter-spacing: .025px;
        
      }
      /* Basic Fluid Image Pattern CSS */
      @media only screen and (max-width: 599px) {
        img.pattern {
          max-width: 100%;
          height: auto !important;
        }
      }
      table {
        border-collapse: collapse;
      }
      table td {
        mso-line-height-rule: exactly;
      }
      .ExternalClass,
      .ExternalClass a,
      .ExternalClass span,
      .ExternalClass b,
      .ExternalClass br,
      .ExternalClass p,
      .ExternalClass div {
        line-height: inherit;
      }
      @media only screen and (max-width:500px) {
        /* default style */
        table[class="flexible"] {
          width: 100% !important;
        }
        table[class="table-center"] {
          float: none !important;
          margin: 0 auto !important;
          width: auto !important;
        }
        *[class="hide"] {
          display: none !important;
          width: 0 !important;
          height: 0 !important;
          padding: 0 !important;
          font-size: 0 !important;
          line-height: 0 !important;
        }
        span[class="db"] {
          display: block !important;
        }
        td[class="img-flex"] img {
          width: 100% !important;
          height: auto !important;
        }
        td[class="aligncenter"] {
          text-align: center !important;
        }
        tr[class="table-holder"] {
          display: table !important;
          width: 100% !important;
        }
        th[class="tcap"] {
          display: table-caption !important;
          width: 100% !important;
        }
        th[class="thead"] {
          display: table-header-group !important;
          width: 100% !important;
        }
        th[class="trow"] {
          display: table-row !important;
          width: 100% !important;
        }
        th[class="tfoot"] {
          display: table-footer-group !important;
          width: 100% !important;
        }
        th[class="flex"] {
          display: block !important;
          width: 100% !important;
        }
        /* custom style */
        td[class="wrapper"] {
          padding: 20px 10px 20px !important;
        }
        td[class="frame"] {
          padding: 20px 30px 40px !important;
        }
        td[class="logo"] img {
          max-width: 150px !important;
        }
        td[class="img-header"] img {
          width: 580px !important;
          height: auto !important;
          padding: 0px 10px 0px 10px !important;
        }
      }
    </style>
  </head>
  <body style="margin:0; padding:0; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;" bgcolor="#f5f7f9">
    <table style="min-width:320px;border-collapse:collapse;" width="100%" cellspacing="0" cellpadding="0" bgcolor="#f5f7f9">

      <!-- fix for gmail -->
      <tr>
        <td style="line-height:0;mso-line-height-rule:exactly;">
          <div style="display:none; white-space:nowrap; font:15px/1px courier;">                                                                 </div>
        </td>
      </tr>
      <tr>
        <td class="wrapper" style="padding:39px 10px 30px;mso-line-height-rule:exactly;">
          <table class="flexible" width="600" align="center" style="margin:0 auto;border-collapse:collapse;" cellpadding="0" cellspacing="0">

            <!-- fix for gmail -->
            <tr>
              <td class="hide" style="mso-line-height-rule:exactly;">
                <table width="600" cellpadding="0" cellspacing="0" style="width:600px !important;border-collapse:collapse;">
                  <tr>
                    <td style="min-width:600px;font-size:0;line-height:0;mso-line-height-rule:exactly;"> </td>
                  </tr>
                </table>
              </td>
            </tr>

            <!-- logo -->
            <tr>
              <td class="logo" align="center" style="padding:0 0 25px;mso-line-height-rule:exactly;"><img src="https://tamulogo.s3.amazonaws.com/tamu_heart.png" width="90" style="width:90px;vertical-align:top;border:none;" alt="Tamu"></td>
            </tr>

            <!-- main -->
            <tr>
              <td bgcolor="#ffffff" style="mso-line-height-rule:exactly;">
                <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">

                  <!-- hero image -->
                  <tr>
                    <td align="center" class="img-flex" style="padding:0px 0 0 0;margin:0;mso-line-height-rule:exactly;">
                        <p style="font-size: 28px;">You have received a gift from </p>
                    </td>
                  </tr>

                  <!-- content -->
                  <tr>
                    <td class="frame" style="padding: 8px 25px 25px;mso-line-height-rule:exactly;">
                      <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">

                        <!-- profile image -->
                        <tr>
                          <td align="center" class="img-flex" style="padding:0px 0 0 0;margin:0;mso-line-height-rule:exactly;"><img src="https://tamulogo.s3.amazonaws.com/tamu_heart.png" width="90" height="80" alt="" style="max-width:110px;vertical-align:top;border:none;border-radius: 50%;">
                          </td>
                        </tr>
                        <tr>
                          <td class="link1" align="center" style="padding:23px 0 0px;font:18px/26px Arial, Helvetica, sans-serif;color:#181A1D;letter-spacing:.025em;mso-line-height-rule:exactly;">
                            """+display_name+"""
                          </td>
                        </tr>
                        <tr>
                          <td class="link1" align="center" style="padding:0px 0 26px;font:13px/26px Arial, Helvetica, sans-serif;color:#777a81;letter-spacing:.025em;mso-line-height-rule:exactly;">
                            {amount}
                          </td>
                        </tr>

                        <!--cta-->
                        <tr align="center">
                          <td align="center" style="mso-line-height-rule:exactly;">
                            <table align="center" cellpadding="0" cellspacing="0" border="0" style="margin:0px auto 0px; border-collapse:collapse;">
                              <tr align="center">
                                <td align="center" style="padding:0px 0px 50px;mso-line-height-rule:exactly;">
                                  <table align="center" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto;border-collapse:collapse;">
                                  </table>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                        
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <!--	<th class="flex" width="20" height="10" style="padding:0;"></th>
													<th class="flex" align="left">
														<table class="table-center" cellpadding="0" cellspacing="0">
															<tr>
																<td width="30" style="line-height:1px; font-size:1px; mso-line-height-rule:at-least;">
																	<img src="http://image.e.onepeloton.com/lib/fe85137272670c7572/m/1/MAIL_ICON.png" width="19" style="vertical-align:top;" alt="" />
																</td>
																<td style="font:14px/21px Arial, Helvetica, sans-serif; color:#a8acb1; letter-spacing:0.3px;">
																	<a style="color:#a8acb1; text-decoration:none;" href="mailto:sales@onepeloton.com">sales@onepeloton.com</a>
																</td>
															</tr>
														</table>
													</th> -->

            <!-- crossell -->

            <!--	<tr>
							<td class="img-flex" style="padding: 20px 0px 0px;"><a href="https://www.onepeloton.com/shop/accessories" alias="HRM" style="text-decoration: none" target="_blank">
								<img src="http://image.e.onepeloton.com/lib/fe85137272670c7572/m/1/HRM_CS.jpg" width="600" height="200" style="width:600px; vertical-align:top;"/></a>
							</td>
						</tr> -->

            <!-- footer -->
            <tr>
              <td style="padding:0px 20px;mso-line-height-rule:exactly;">
                <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
                  
                  <tr>
                    <td style="padding:20px 0 27px;mso-line-height-rule:exactly;">
                      
                    </td>
                  </tr>
                  <table align="center" border="0" cellpadding="0" cellspacing="0" class="template-text-container" style="max-width: 100%; min-width: 100%; border-collapse: collapse; mso-table-lspace: 0; mso-table-rspace: 0; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                    <tbody>
                      <tr>
                        <td valign="top" class="template-text-content" style="word-break:break-word;color:#777A81;font-family:Arial, Helvetica, sans-serif;font-size:13px;line-height:22px;font-weight:300;padding:0 80px 10px;mso-line-height-rule:exactly;" align="center">

                          <!-- TEXT CONTENT GOES HERE, IT'S RECOMMENDED TO WRAP THE TEXT INSIDE A <h1>, <h2>, <hx.... OR A <p> tag -->
                          © 2023 Tamu
                           </td>
                      </tr>
                    </tbody>
                  </table>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    </body>
</html>
    """

    return mail_sub

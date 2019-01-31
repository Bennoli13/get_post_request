<p><strong>REQUEST (GET &amp; POST)</strong></p>
<p>This code is to do GET REQUEST from sFlow-RT API and POST REQUEST to local database every 60 second. Wrote on Jupyter Notebook version 5.7.4 with Python version 3.7.1 then downloaded as python code.</p>
<p><em>INFORMATION :</em></p>
<p>SFlow-RT implemented in SDN Network to collect the sample packet data in the network. In order to analyze the captured packet data, I made 2 flows in the SFlow-RT server, TCP and UDP.</p>
<p>TCP features are :</p>
<ol>
<li>ipsource</li>
<li>ipdestination</li>
<li>tcpsourceport</li>
<li>tcpdestinationport</li>
<li>tcpflags</li>
<li>tcpwindow</li>
<li>tcppayloadbytes</li>
<li>tcpseqno</li>
<li>tcpackno</li>
<li>bytes</li>
</ol>
<p>UDP features are :</p>
<ol>
<li>ipsource</li>
<li>ipdestination</li>
<li>udpsourceport</li>
<li>udpdestinationport</li>
<li>udpbytes</li>
<li>bytes</li>
</ol>
<p>Then the database structure follows those features which mentioned above.&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;</p>

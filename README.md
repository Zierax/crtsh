<h1>crtsh</h1>

<p>A command-line tool to find subdomains using crt.sh API.</p>

<h2>Usage</h2>

<pre><code>python3 crtsh.py -d example.com [-r] [-w]</code></pre>

<h2>Options</h2>

<ul>
    <li><code>-d, --domain &lt;domain&gt;</code>: Specify the target domain to fetch subdomains from crt.sh (required).</li>
    <li><code>-r, --recursive</code>: Perform a recursive search for subdomains.</li>
    <li><code>-w, --wildcard</code>: Include wildcard subdomains in the output.</li>
</ul>

<h2>Installation</h2>

<p>Clone the repository and install dependencies:</p>

<pre><code>git clone https://github.com/yourusername/subdomain-finder.git
cd subdomain-finder
pip install -r requirements.txt
</code></pre>

<h2>Dependencies</h2>

<ul>
    <li><a href="https://pypi.org/project/requests/">Requests</a>: HTTP library for making API requests.</li>
</ul>

<h2>Example</h2>

<pre><code>python3 subdomain_finder.py -d google.com -r -w</code></pre>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contributing</h2>

<p>Contributions are welcome! Please fork the repository and submit a pull request with your improvements.</p>

<h2>Acknowledgments</h2>

<p>Thanks to crt.sh for providing the subdomain search API.</p>

</body>
</html>
